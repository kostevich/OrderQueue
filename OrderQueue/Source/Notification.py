
#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from dublib.Methods import ReadJSON
from telethon import TelegramClient


import asyncio

#==========================================================================================#
# >>>>> ЧТЕНИЕ НАСТРОЕК <<<<< #
#==========================================================================================#

Settings = ReadJSON("Source\Settings.json")

#==========================================================================================#
# >>>>> НАСТРОЙКА ТЕЛЕГРАММ КЛИЕНТА <<<<< #
#==========================================================================================#

client = TelegramClient('bot', Settings["api_id"], Settings["api_hash"]).start(bot_token=Settings["token"])

async def mavin():
    entity = await client.get_entity('url')
    entity = await client.get_entity('number')
    # await client.send_message(entity, 'Hello, friend!')
    print(entity)

    
with client:
    client.loop.run_until_complete(mavin())

# asyncio.run(mavin())