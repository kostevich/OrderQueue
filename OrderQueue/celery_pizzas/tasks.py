
#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from celery import shared_task
from celery.utils.log import get_task_logger
from Source.Functions import *
from Source.Notification import *

import asyncio
import time
import random

#==========================================================================================#
# >>>>> СОЗДАНИЕ ЛОГГИРОВАНИЯ  <<<<< #
#==========================================================================================#

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
                
                # Добавляем в json формат данные о подтверждении заказа.
                InfoOrders["Queue"][Queue]["Confirmation"] = True

                # Добавляем в json формат данные о статусе заказа.            
                InfoOrders["Queue"][Queue]["Status"] = "Заказ готовится"

                # Логгирование.
                logger.info('Заказ подтверждён')

                # Номер телефона заказчика.
                phonenumber = (InfoOrders["Queue"][Queue]["User"][0]["PhoneNumber"])

                # Текст уведомлени для заказчика.
                textmessage = "Ваш заказ готовиться: ссылка для трекинга."

                # Уведомление о начале готовки.
                asyncio.run(SendMessage(str(phonenumber), textmessage))

                # Логгирование.
                logger.info('Уведомление о готовке заказа отправлено.')
                
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

                # Логгирование.
                logger.info('Заказ удалён')
                
    # Запись в json формат.
    InfoOrdersWrite(InfoOrders)
     


    

      