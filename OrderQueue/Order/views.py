from django.shortcuts import render
from Source.Menu import InfoPizzas
from dublib.Methods import WriteJSON
# Create your views here.

# InfoOrders = {
#     'Orders': []
# }

def MainPage(request):
    context = {'InfoPizzas': InfoPizzas["Pizzas"]}
    return render(request, "main.html", context)

def AboutPage(request):
    return render(request, "about.html")

def PreOrderPage(request):
    if request.method == 'POST':
      idorder = request.POST["idorder"]
      nameorder = request.POST["nameorder"]
      priceorder = request.POST["priceorder"]
      countpizzas = request.POST["countpizzas"]
      dict = {
         'idorder': idorder,
         'nameorder': nameorder, 
         'priceorder': priceorder, 
         'countpizzas': countpizzas
      }
      return render(request, 'preorder.html', dict)   

 

