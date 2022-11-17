from django.shortcuts import render, get_object_or_404, redirect 
from belly.get_data import api_response
from django.db.models import Q
from belly.models import Menu
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from belly.models import Menu 
import random

@cache_page(60 * 60)
@vary_on_cookie
def index(request):
    search_post = request.GET.get('search')
    if search_post:
        menu_list = Menu.objects.filter(Q(menu_name__icontains=search_post) & \
            Q(description__icontains=search_post) & Q(ingredients__icontains=search_post))  
    else:
        menu_list = Menu.objects.all().order_by('-id')[:24]
    feed = api_response()
    for entry in feed:
        try:
            get_menu_name = entry['display']['displayName']
        except:
            get_menu_name = 'missing menu name'

        try:
            get_kcal = [element['value'] for element \
                in entry['content']['nutrition']['nutritionEstimates'] \
                    if element['attribute'] == 'ENERC_KCAL'][0]
        except:
            get_kcal = -99
        try:
            get_fat = [element['value'] for element \
                in entry['content']['nutrition']['nutritionEstimates'] \
                    if element['attribute'] == 'FAT_KCAL'][0]
        except:
            get_fat = -99
        try:
            get_sugar = [element['value'] for element \
                in entry['content']['nutrition']['nutritionEstimates'] \
                    if element['attribute'] == 'SUGAR'][0]
        except:
            get_sugar = -99

        try:
            get_picture_url = entry['display']['images'][0]
        except:
            get_picture_url = ''

            
        menu = Menu(
            menu_name= get_menu_name,
            energy_kcal = get_kcal,
            fat_kcal = get_fat,
            sugar = get_sugar,
            picture_url = get_picture_url,
        )
        if menu not in Menu.objects.all() \
            and menu.menu_name != 'missing menu name':
            menu.save()
    
    
    return render(request, 'belly/index.html', {"menu_list": menu_list})
