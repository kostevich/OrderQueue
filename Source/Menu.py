from bs4 import BeautifulSoup
from dublib.Methods import WriteJSON

import requests 

# Словарь со всей информацией по пиццам.
InfoPizzas = dict() 
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
    allNames =  item.find('div', {'class': 'product-card__title'}).text
    allIngridients =  item.find('div', {'class': 'product-card__description'}).text
    allSizePizzas =  item.find('p', {'class': 'product-card__modification-info-weight'}).text
    allPricePizzas =  item.find('p', {'class': 'product-card__modification-info-price'}).text
    # Запись данных в словарь.
    InfoPizzas[ID] = {'Name': allNames, 'Ingridients': allIngridients, 'Size': allSizePizzas, 'Price': allPricePizzas}

# Смена ID.
ID = 0


for item in AllImages:
    # Смена ID.
    ID +=1
    # Вывод изображений пиццы.
    allUrlImages = item["src"]
    # Обновление данных в словаре.
    InfoPizzas[ID].update({'Images': allUrlImages})
        
# Запись словаря в JSON.
WriteJSON('InfoPizzas.json', InfoPizzas)
