
#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from dublib.Methods import ReadJSON
from telethon import functions
from telethon import TelegramClient
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.types import InputPhoneContact

#==========================================================================================#
# >>>>> ЧТЕНИЕ НАСТРОЕК <<<<< #
#==========================================================================================#

Settings = ReadJSON("Source\Settings.json")

#==========================================================================================#
# >>>>> ОТПРАВКА УВЕДОМЛЕНИЙ <<<<< #
#==========================================================================================#

async def SendMessage(phonenumber, textmessage):
    # Настройка телеграмм-клиента.
    async with TelegramClient('anon', Settings["api_id"], Settings["api_hash"]) as client:
        # Аутентифицируемся.
        await client.start()

        # Если заказчик наш контакт пробуем отправить по номеру телефона.
        try:
            # Отправка уведомления по номеру телефона.
            await client.send_message(str(phonenumber), textmessage)
        
        except:
            # Создание данных контакта.
            contact = InputPhoneContact(client_id=0, phone=phonenumber, first_name="Уведомление", last_name="Отправлено")
            
            # Добавление контакта.
            contacts = await client(ImportContactsRequest([contact]))

            # Отправка уведомления по номеру телефона.
            await client.send_message(phonenumber, textmessage)

            # Удаление контакта.
            await client(functions.contacts.DeleteContactsRequest([contacts.users[0]]))
