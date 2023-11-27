from celery import Celery
from Source.Functions import *
from Source.Broker import *

import random
import time
import os

app = Celery('OrderQueue', broker=broker, backend='rpc://')

@app.task
def OrderConfirmation(InfoOrders):
   for Queue in range(len(InfoOrders['Queue'])):
      if 'Confirmation' not in InfoOrders["Queue"][Queue].keys():
         Confirmation = random.randint(1, 10)
         print(Confirmation)
         if Confirmation < 9:
            InfoOrders["Queue"][Queue]["Confirmation"] = True
            if Confirmation<3:
               InfoOrders["Queue"][Queue]["Payment"] = "Оплата картой(курьеру)"
            elif Confirmation<5 and Confirmation>3:
               InfoOrders["Queue"][Queue]["Payment"] = "Оплата наличными"
            else:
               InfoOrders["Queue"][Queue]["Payment"] = "Оплата картой(на сайте)"
         else: 
            del InfoOrders["Queue"][Queue]
      print('dsd')
      WriteJSON('json/InfoOrders.json', InfoOrders)  
      return InfoOrders  

            

   
         