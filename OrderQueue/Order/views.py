from django.shortcuts import render
from Source.Menu import InfoPizzas, IDList

# Create your views here.

def MainPage(request):
    context = {'InfoPizzas': InfoPizzas , 'IDList': IDList}
    return render(request, "main.html", context)

def AboutPage(request):
    return render(request, "about.html")

def PreOrderPage(request):
    return render(request, "preorder.html")