
#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from celery import shared_task
from celery.utils.log import get_task_logger
from Source.Functions import *

import time
import random

logger = get_task_logger(__name__)
#==========================================================================================#
# >>>>> TASK: ПОДТВЕРЖДЕНИЕ ЗАКАЗА  <<<<< #
#==========================================================================================#

@shared_task
def OrderConfirmation(InfoOrders):
    logger.info('Подтверждение заказа')
    for Queue in range(len(InfoOrders['Queue'])):
        # Если нет поля подтверждения заказа.
        if 'Confirmation' not in InfoOrders["Queue"][Queue].keys():
            Confirmation = random.randint(1, 10)

            # Создание одобрения подтверждения заказа.
            if Confirmation < 9:
                InfoOrders["Queue"][Queue]["Confirmation"] = True
                logger.info('Заказ подтверждён')

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
                logger.info('Заказ удалён')
    # Запись в json формат.
    WriteJSON('json/InfoOrders.json', InfoOrders)  
    time.sleep(20)
    return InfoOrders  


@shared_task
def Notifications():
    logger.info('Отправка уведомления')
      