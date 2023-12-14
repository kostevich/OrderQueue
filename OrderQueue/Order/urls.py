
#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from django.urls import path
from . import views

#==========================================================================================#
# >>>>>  ЛОКАЛЬНЫЕ ССЫЛКИ ДЛЯ РАБОТЫ САЙТА <<<<< #
#==========================================================================================#

urlpatterns = [
    path('', views.MainPage, name='MainPage'),
    path('about', views.AboutPage, name='AboutPage'),
    path('preorder', views.PreOrderPage, name='PreOrderPage'),
    path('form', views.FormPage, name='FormPage'),
    path('orders', views.SendForm, name='SendForm'),
]