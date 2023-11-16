from celery import Celery
from .Functions import *
from .Broker import *

import random
import time


app = Celery('myapp', broker=broker)


@app.task
def OrderConfirmation(InfoOrders):
   for Queue in range(len(InfoOrders['Queue'])):
      if 'Confirmation' not in InfoOrders["Queue"][Queue].keys():
         Confirmation = random.randint(1, 10)
         time.sleep(12)
         if Confirmation < 9:
            InfoOrders["Queue"][Queue]["Confirmation"] =  True
         else: 
            print(InfoOrders["Queue"][Queue])
            del InfoOrders["Queue"][Queue]
   WriteJSON('json/InfoOrders.json', InfoOrders)    

            

   
         