from bs4 import BeautifulSoup
from .Functions import *

import requests 

def ReceiveMenu():
    # Словарь со всей информацией по пиццам.
    InfoPizzas = {
        "Pizzas": []
    }
    # Начальное id пиццы.
    ID = 0

    # Ccылка на страницу с данными пицц.
    url = "https://dominos.by/pizza"
    # Запрос к сайту.
    Menu = requests.get(url)

    # Сохранение html.
    soup = BeautifulSoup(Menu.text, "html.parser")

    # Поиск данных в классах на странице.   
    AllPizzas =  soup.find_all('div', {"class": "product-card__content"})
    AllImages =  soup.find_all('img', {"class": "media-image__element product-card-media__element"})


    for item in AllPizzas:
        # Смена ID.
        ID +=1
        # Вывод текстовых данных о пицце.
        allNames =  item.find('div', {'class': 'product-card__title'}).text.replace("new", "").replace("хит", "")
        allIngridients =  item.find('div', {'class': 'product-card__description'}).text
        allSizePizzas =  item.find('p', {'class': 'product-card__modification-info-weight'}).text.replace(" гр", "")
        allPricePizzas =  item.find('p', {'class': 'product-card__modification-info-price'}).text.replace(" руб.", "")
        # Запись данных в словарь.
        InfoPizzas["Pizzas"].append({'Id': ID, 'Name': allNames, 'Ingridients': allIngridients, 'Size': int(allSizePizzas), 'Price': float(allPricePizzas)})


    for i in range(len(AllImages)):
        # Вывод изображений пиццы.
        allUrlImages = AllImages[i]["src"]
        # Обновление данных в словаре.
        InfoPizzas["Pizzas"][i]['Images'] = allUrlImages
    return InfoPizzas


