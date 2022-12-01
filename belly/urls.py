from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign-up', views.sign_up, name='sign-up'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name="logout"),
    path('choose', views.choose, name="choose"),
    path('choose_one', views.choose_one, name="choose_one"),
    path('choose_two', views.choose_two, name="choose_two"),
    path('choose_three', views.choose_three, name="choose_three"),
]
