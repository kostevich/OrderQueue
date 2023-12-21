
#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from dublib.Methods import ReadJSON
from telethon import TelegramClient
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.types import InputPhoneContact


import asyncio
import logging

#==========================================================================================#
# >>>>> ЧТЕНИЕ НАСТРОЕК <<<<< #
#==========================================================================================#

Settings = ReadJSON("Source\Settings.json")

#==========================================================================================#
# >>>>> НАСТРОЙКА ТЕЛЕГРАММ КЛИЕНТА <<<<< #
#==========================================================================================#


with TelegramClient('anon', Settings["api_id"], Settings["api_hash"]) as client:
    client.loop.run_until_complete(client.send_message('me', '1!'))


# client = TelegramClient('bot', Settings["api_id"], Settings["api_hash"]).start(bot_token=Settings["token"])


async def mavin():
    entity1 = await client.get_entity('https://t.me/sleep_fox789')
    await client.send_message(entity1, '2')
    await client.send_message('+375295827818', 'Hello, friend!')
    # contact = InputPhoneContact(client_id=0, phone="+375295827816", first_name="", last_name="")
    # result = client(ImportContactsRequest([contact]))
    # await client.send_message('+375295827816', 'Hello, friend1!')
    
with client:
    client.loop.run_until_complete(mavin())

