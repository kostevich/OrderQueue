from bs4 import BeautifulSoup

import requests 


url = "https://dominos.by/pizza"
Menu = requests.get(url)
AllPizzas = []
AllInformation = []

soup = BeautifulSoup(Menu.text, "html.parser")
Allimages =  soup.find_all('img', class_= "media-image__element product-card-media__element")
for item in Allimages:
    UrlImage = str(item).split("src=")[1]


AllPizzas =  soup.find_all('div', class_= "product-card__content")

for item in AllPizzas:
    allNames =  item.find('div', {'class': 'product-card__title'}).text
    allIngridients =  item.find('div', {'class': 'product-card__description'}).text
    allSizePizzas =  item.find('p', {'class': 'product-card__modification-info-weight'}).text
    allPricePizzas =  item.find('p', {'class': 'product-card__modification-info-price'}).text