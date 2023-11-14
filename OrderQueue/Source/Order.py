from celery import Celery
from .Functions import *
from Order.models import Order

app = Celery('myapp', broker='http://127.0.0.1:8000/')


@app.task
def RakingOrders(InfoOrders):
   NamePizzas = list()
   if len(InfoOrders["Orders"]) != 0:
      for Orders in range(len(InfoOrders["Orders"])):
         for i in range(len(InfoOrders["Orders"][Orders]["Pizzas"])):
            NamePizzas.append({InfoOrders["Orders"][Orders]["Pizzas"][i]["Name"]:InfoOrders["Orders"][Orders]["Pizzas"][i]["Count"]})
            print(NamePizzas)
         Order.objects.create(
            Time = str(InfoOrders["Orders"][Orders]["Datetime"]),
            IdOrder = InfoOrders["Orders"][Orders]["Id"],
            NameUser = str(InfoOrders["Orders"][Orders]["User"][0]["Name"]),
            Adress = str(InfoOrders["Orders"][Orders]["User"][0]["Adress"]),
            PhoneNumber = str(InfoOrders["Orders"][Orders]["User"][0]["PhoneNumber"]),
            TotalPrice = InfoOrders["Orders"][Orders]["TotalPrice"],
            NamePizza = NamePizzas,
            Count = 3,
         )
   else: 
      pass