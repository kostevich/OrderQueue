from celery import Celery
from Source.Functions import *
from Source.Broker import *

import random
import time
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cel.settings')

app = Celery('cel', broker=broker)

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task
def OrderConfirmation(InfoOrders):
   for Queue in range(len(InfoOrders['Queue'])):
      if 'Confirmation' not in InfoOrders["Queue"][Queue].keys():
         Confirmation = random.randint(1, 10)
         print(Confirmation)
         time.sleep(12)
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
      WriteJSON('json/InfoOrders.json', InfoOrders)  
      print(InfoOrders)  

            

   
         