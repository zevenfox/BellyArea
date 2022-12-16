from django.shortcuts import render, get_object_or_404, redirect
from belly.get_data import api_response
from django.db.models import Q
from belly.models import Menu
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from belly.models import Menu, TopPick, Graph
import random

from django.core import serializers
import json
from .models import User
from django.contrib import messages
from .decorators import unauthenticated_user, allowed_users
from django.views.decorators.csrf import csrf_exempt
from collections import Counter


@csrf_exempt
@cache_page(60 * 60)
@vary_on_cookie
def index(request):
    if request.method == 'POST':
        try:
            if request.session['user']:
                request.session['age'] = 0
                request.session['who'] = ""
                request.session['sex'] = ""
                menulist = request.POST.getlist('menu')
                sex = request.POST.getlist('sex')
                age = request.POST.getlist('age')
                request.session['age'] = age[0]
                request.session['sex'] = sex[0]

                if int(age[0]) <= 17:
                    request.session['who'] = "ควรออกกำลังกายปานกลางถึงหนัก อย่างน้อย 60 นาทีต่อสัปดาห์"
                elif int(age[0]) >= 18 and int(age[0]) <= 64:
                    request.session['who'] = "ควรออกกำลังกายอย่างน้อย 150 นาที หรือ 2.5 ชั่วโมงต่อสัปดาห์"
                elif int(age[0]) >= 65:
                    request.session['who'] = "ออกกำลังกาย 150-300 นาทีต่อสัปดาห์ด้วยกิจกรรมออกกำลังกายระดับปานกลาง"

                data_food = ""
                for i in range(len(menulist)):
                    if i == len(menulist) - 1:
                        data_food += menulist[i]
                    else:
                        data_food += (menulist[i] + ",")

                cal = 0
                for i in menulist:
                    m = list(Menu.objects.all().filter(
                        menu_name=i).values_list('energy_kcal'))
                    print(m[0][0])
                    cal += float(m[0][0])


                if sex[0] == "female":
                    if int(age[0]) >= 1 and int(age[0]) <= 12:
                        age_e = "1 - 12"
                        should_eat = 1200
                    elif int(age[0]) >= 13 and int(age[0]) <= 21:
                        age_e = "13 - 21"
                        should_eat = 2000
                    elif int(age[0]) >= 22 and int(age[0]) <= 45:
                        age_e = "22 - 45"
                        should_eat = 1800
                    elif int(age[0]) >= 46 and int(age[0]) <= 60:
                        age_e = "46 - 60"
                        should_eat = 1600
                    elif int(age[0]) > 60:
                        age_e = "> 60"
                        should_eat = 1500
                else:
                    if int(age[0]) >= 1 and int(age[0]) <= 12:
                        age_e = "1 - 12"
                        should_eat = 1100
                    elif int(age[0]) >= 13 and int(age[0]) <= 21:
                        age_e = "13 - 21"
                        should_eat = 2100
                    elif int(age[0]) >= 22 and int(age[0]) <= 45:
                        age_e = "22 - 45"
                        should_eat = 1900
                    elif int(age[0]) >= 46 and int(age[0]) <= 60:
                        age_e = "46 - 60"
                        should_eat = 1600
                    elif int(age[0]) > 60:
                        age_e = "> 60"
                        should_eat = 1400

                if int(age[0]) >= 1:
                    c = cal - should_eat
                    if c <= 0:
                        c = 0
                        p = 0
                    else:
                        p = 0
                        while c >= 100:
                            c -= 100
                            p += 1

                    g = Graph.objects.create(age=age_e, point=p, sex=sex[0])
                    g.save()
                print(cal)

                top = TopPick.objects.create(
                    age=age[0],
                    food=data_food,
                    sex=sex[0],
                )
                top.save()

                return redirect('/choose')
        except:
            return redirect('/login')
    search_post = request.GET.get('search')
    if search_post:
        menu_list = Menu.objects.filter(Q(menu_name__icontains=search_post) & Q(
            description__icontains=search_post) & Q(ingredients__icontains=search_post))
    else:
        menu_list = Menu.objects.all().order_by('-id')[:24]
    feed = api_response()
    for entry in feed:
        try:
            get_menu_name = entry['display']['displayName']
        except:
            get_menu_name = 'missing menu name'

        try:
            get_kcal = [element['value'] for element in entry['content']['nutrition']['nutritionEstimates']
                        if element['attribute'] == 'ENERC_KCAL'][0]
        except:
            get_kcal = -99
        try:
            get_fat = [element['value'] for element in entry['content']['nutrition']['nutritionEstimates']
                       if element['attribute'] == 'FAT_KCAL'][0]
        except:
            get_fat = -99
        try:
            get_sugar = [element['value'] for element in entry['content']['nutrition']['nutritionEstimates']
                         if element['attribute'] == 'SUGAR'][0]
        except:
            get_sugar = -99

        try:
            get_picture_url = entry['display']['images'][0]
        except:
            get_picture_url = ''

        menu = Menu(
            menu_name=get_menu_name,
            energy_kcal=get_kcal,
            fat_kcal=get_fat,
            sugar=get_sugar,
            picture_url=get_picture_url,
        )
        if menu not in Menu.objects.all() and menu.menu_name != 'missing menu name':
            menu.save()
    try:
        data = request.session['user']['username']
    except:
        data = ""
    return render(request, 'belly/index.html', {"menu_list": menu_list, "username": data})


@allowed_users(allowed_roles=['user'])
def choose(request):
    return render(request, 'belly/choose.html')


@allowed_users(allowed_roles=['user'])
def choose_one(request):
    return render(request, 'belly/choose_one.html', {"data": request.session['who']})


@allowed_users(allowed_roles=['user'])
def choose_two(request):
    data = list(TopPick.objects.all().filter(
        age=request.session['age'], sex=request.session['sex']).values_list('age', 'food', 'sex'))
    data_rate = []
    for x in data:
        f = x[1].split(',')
        for i in f:
            data_rate.append(i)

    dd = Counter(data_rate)
    key_list = list(dd.keys())[:5]

    return render(request, 'belly/choose_two.html', {"data": key_list})


@allowed_users(allowed_roles=['user'])
def choose_three(request):

    graph = list(Graph.objects.all().values_list('age', 'point', 'sex'))

    m_1 = 0
    m_2 = 0
    m_3 = 0
    m_4 = 0
    m_5 = 0
    f_1 = 0
    f_2 = 0
    f_3 = 0
    f_4 = 0
    f_5 = 0

    for item in graph:
        if item[2] == "male":
            if item[0] == "1 - 12":
                m_1 += int(item[1])
            elif item[0] == "13 - 21":
                m_2 += int(item[1])
            elif item[0] == "22 - 45":
                m_3 += int(item[1])
            elif item[0] == "46 - 60":
                m_4 += int(item[1])
            elif item[0] == "> 60":
                m_5 += int(item[1])
        else:
            if item[0] == "1 - 12":
                f_1 += int(item[1])
            elif item[0] == "13 - 21":
                f_2 += int(item[1])
            elif item[0] == "22 - 45":
                f_3 += int(item[1])
            elif item[0] == "46 - 60":
                f_4 += int(item[1])
            elif item[0] == "> 60":
                f_5 += int(item[1])

    print(m_1, m_2, m_3, m_4, m_5, f_1, f_2, f_3, f_4, f_5)
    return render(request, 'belly/choose_three.html', {"m1": m_1, "m2": m_2, "m3": m_3, "m4": m_4,"m5": m_5, "f1": f_1, "f2": f_2, "f3": f_3, "f4": f_4, "f5": f_5})


@unauthenticated_user
def sign_up(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password_c = request.POST['password_c']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Sorry! username is taken.')
            return redirect('/sign-up')
        elif password != password_c:
            messages.error(request, 'Sorry! passwords do not match.')
            return redirect('/sign-up')
        else:
            user = User.objects.create(
                email=email,
                username=username,
                password=password,
            )
            user.save()
            messages.info(request, 'Created successfully.')
            return redirect('/sign-up')
    else:
        return render(request, "belly/sign-up.html")


@unauthenticated_user
def login(request):
    if request.method == 'POST':
        login_email = request.POST['email']
        login_password = request.POST['password']

        user = User.objects.filter(
            email=login_email, password=login_password
        )
        if len(user) > 0:
            user = serializers.serialize("json", User.objects.filter(
                email=login_email, password=login_password
            ))
            request.session['user'] = json.loads(user)[0]['fields']

            return redirect('/')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('/login')

    else:
        return render(request, "belly/login.html")


@allowed_users(allowed_roles=['user'])
def logout(request):
    del request.session['user']

    messages.info(request, 'You logged out.')
    return redirect('/login')
