from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage, name='MainPage'),
    path('about', views.AboutPage, name='AboutPage'),
    path('preorder', views.PreOrderPage, name='PreOrderPage'),
]