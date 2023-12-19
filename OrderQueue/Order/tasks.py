
#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from celery import shared_task
from Source.Functions import *


import random

#==========================================================================================#
# >>>>> TASK: ПОДТВЕРЖДЕНИЕ ЗАКАЗА  <<<<< #
#==========================================================================================#

@shared_task
def OrderConfirmation(InfoOrders):
    print(1)
    for Queue in range(len(InfoOrders['Queue'])):
        # Если нет поля подтверждения заказа.
        if 'Confirmation' not in InfoOrders["Queue"][Queue].keys():
            Confirmation = random.randint(1, 10)
        # Создание одобрения подтверждения заказа.
        if Confirmation < 9:
            InfoOrders["Queue"][Queue]["Confirmation"] = True
            # Создание поля способа оплаты заказа.
            if Confirmation<3:
                InfoOrders["Queue"][Queue]["Payment"] = "Оплата картой(курьеру)"

            elif Confirmation<5 and Confirmation>3:
                InfoOrders["Queue"][Queue]["Payment"] = "Оплата наличными"

            else:
                InfoOrders["Queue"][Queue]["Payment"] = "Оплата картой(на сайте)"
          # Удалить из заказов.
        else: 
            del InfoOrders["Queue"][Queue]
    # Запись в json формат.
    WriteJSON('json/InfoOrders.json', InfoOrders)  

    return InfoOrders  


@shared_task
def pri():
    fp = open('sales_2.txt', 'w')
    fp.write('first line')
    fp.close()