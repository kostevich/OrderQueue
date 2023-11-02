from django.shortcuts import render
from Source.Menu import InfoPizzas

# Create your views here.

def MainPage(request):
    context = {'InfoPizzas': InfoPizzas["Pizzas"]}
    return render(request, "main.html", context)

def AboutPage(request):
    return render(request, "about.html")

def PreOrderPage(request):
    return render(request, "preorder.html")