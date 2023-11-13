from celery import Celery
from .Functions import *
from Order.models import Order

app = Celery('myapp', broker='http://127.0.0.1:8000/')


@app.task
def RakingOrders(InfoOrders):
   if len(InfoOrders["Queue"]) != 0:
      for Orders in range(len(InfoOrders["Queue"])):
         for i in range(len(InfoOrders["Queue"][Orders]["Pizzas"])):
            Order.objects.create(
               Time = str(InfoOrders["Queue"][Orders]["Datetime"]),
               IdOrder = InfoOrders["Queue"][Orders]["Id"],
               NameUser = str(InfoOrders["Queue"][Orders]["User"][0]["Name"]),
               Adress = str(InfoOrders["Queue"][Orders]["User"][0]["Adress"]),
               PhoneNumber = str(InfoOrders["Queue"][Orders]["User"][0]["PhoneNumber"]),
               TotalPrice = str(InfoOrders["Queue"][Orders]["TotalPrice"]),
               NamePizza = str(InfoOrders["Queue"][Orders]["Pizzas"][i]["Name"]),
               Count = InfoOrders["Queue"][Orders]["Pizzas"][i]["Count"]
               )
   else: 
      pass