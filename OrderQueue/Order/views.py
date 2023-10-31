from django.shortcuts import render
import sys
sys.path.insert(0, "C:\Data storage\Programming\Internship\OrderQueue\Source")
from Menu import InfoPizzas, IDList

# Create your views here.

def MainPage(request):
    context = {'InfoPizzas': InfoPizzas , 'IDList': IDList}
    return render(request, "main.html", context)

def AboutPage(request):
    return render(request, "about.html")

def PreOrderPage(request):
    return render(request, "preorder.html")