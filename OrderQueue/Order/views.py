from django.shortcuts import render
from Source.Functions import *
from Source.Menu import *
import os

path = 'C:\Data storage\Programming\Internship\OrderQueue\OrderQueue\json'


def MainPage(request):
    if os.path.exists(path + '/InfoOrders.json'):
        InfoOrders = InfoOrdersRead()
    else:
        InfoOrders = {'Orders': []} 
        InfoOrdersWrite(InfoOrders)


    if os.path.exists(path + '/AllPrice.json'):
        AllPrice = AllPriceRead()
    else: 
        AllPrice = {'AllPrice': '0 руб.' }
        AllPriceWrite(AllPrice)


    if os.path.exists(path + '/InfoPizzas.json'):  
        InfoPizzas = InfoPizzasRead()
    else:
        InfoPizzas = ReceiveMenu()
        InfoPizzasWrite(InfoPizzas)
        

    # Словарь добавления в корзину.
    AddOrder = {'id': "0", 'text': ''}
    
    # Если нажата кнопка в корзину и количество выбранных пицц больше 0.
    if request.method =='POST' and int(request.POST["countpizzas"])>0:

        # Если ничего не добавлено в корзину.
        if len(InfoOrders['Orders']) == 0:
            # Общая цена всех пицц в корзине.
            AllPrice['AllPrice'] = float(str(request.POST["countpizzas"]))*float(str(request.POST["priceorder"].split(' ')[0]))
            # Добавить данные о пицце в корзине.
            InfoOrders["Orders"].append({'idorder': request.POST["idorder"],
                                    'nameorder': request.POST["nameorder"],
                                    'priceorder': request.POST["priceorder"],
                                    'countpizzas': request.POST["countpizzas"],
                                    'pricepizza': str(float(str(request.POST["countpizzas"]))*float(str(request.POST["priceorder"].split(' ')[0])))+ ' руб.'})
            
        # Если в корзине что-то есть.
        else:
            # Количество словарей в списке корзины.
            for i in range(len(InfoOrders['Orders'])):
                # Если id пиццы совпадает с id имеющегося словаря.
                if request.POST["idorder"] in InfoOrders['Orders'][i]["idorder"]:
                    # Изменяем количество однотипных пицц в корзине.
                    InfoOrders["Orders"][i]["countpizzas"] = str(int(InfoOrders['Orders'][i]["countpizzas"])+int(request.POST["countpizzas"]))
                    # Изменяем цену однотипных пицц в корзине.
                    InfoOrders["Orders"][i]["pricepizza"]= str(int(str(InfoOrders["Orders"][i]["countpizzas"]))*float(str(request.POST["priceorder"]).split(' ')[0])) + ' руб.'
                    # Выйти из цикла.
                    break


            else:
                # Добавить данные о пицце в корзине.
                InfoOrders["Orders"].append({'idorder': request.POST["idorder"],
                                'nameorder': request.POST["nameorder"],
                                'priceorder': request.POST["priceorder"],
                                'countpizzas': request.POST["countpizzas"],
                                'pricepizza':  str(int(request.POST["countpizzas"])*float(str(request.POST["priceorder"]).split(' ')[0]))+ ' руб.'})
        # Если в корзине что-то есть.
        if len(InfoOrders['Orders']) != 0:
            # Обнуление словаря.
            AllPrice['AllPrice'] = 0
            # Количество словарей в списке корзины.
            for i in range(len(InfoOrders['Orders'])):
                # Расчет общей цены в корзине.
                AllPrice['AllPrice'] += float(str(InfoOrders['Orders'][i]['pricepizza'].split(' ')[0]))
            AllPrice['AllPrice'] = str(round(AllPrice['AllPrice'], 2)) + ' руб.'


        # Добавляем текст при нажатии на кнопку.
        AddOrder = {'id': request.POST["idorder"], 'text': 'Пицца добавлена в корзину'}


        
    # Отображение контента на странице.
    context = {'InfoPizzas': InfoPizzas["Pizzas"], 'AddOrder': AddOrder}
    

    InfoOrdersWrite(InfoOrders)
    AllPriceWrite(AllPrice)

    # Вывод данных на главной странице.
    return render(request, "main.html", context)


def AboutPage(request):
    return render(request, "about.html")


def PreOrderPage(request):
    AllPrice = AllPriceRead()
    InfoOrders = InfoOrdersRead()
    
    if request.method =='POST':
        for i in range(len(InfoOrders["Orders"])):
            if InfoOrders["Orders"][i]["idorder"] == request.POST["idorder"] and InfoOrders["Orders"][i]["countpizzas"] == request.POST["countpizzas"]:
                AllPrice['AllPrice'] = str(round(float(str(AllPrice['AllPrice'].split(' ')[0])) - float(str(InfoOrders['Orders'][i]['pricepizza'].split(' ')[0])), 2)) + ' руб.'
                del InfoOrders["Orders"][i]
                break
            else:
                AllPrice['AllPrice'] = str(round(float(str(AllPrice['AllPrice'].split(' ')[0])) - (float(str(InfoOrders['Orders'][i]['priceorder'].split(' ')[0]))*float(str(request.POST["countpizzas"].split(' ')[0]))), 2)) + ' руб.'
                InfoOrders["Orders"][i]['pricepizza'] = str(round(float(str(AllPrice['AllPrice'].split(' ')[0])) - (float(str(InfoOrders['Orders'][i]['priceorder'].split(' ')[0]))*float(str(request.POST["countpizzas"].split(' ')[0]))), 2)) + ' руб.'
                InfoOrders["Orders"][i]['countpizzas'] = int(InfoOrders["Orders"][i]['countpizzas']) - int(request.POST["countpizzas"])
                break

    InfoOrdersWrite(InfoOrders)     
    AllPriceWrite(AllPrice)

    # Отображение контента на странице.
    context = {'InfoOrders': InfoOrders["Orders"],'AllPrice': AllPrice}

    # Вывод данных на главной странице.
    return render(request, "preorder.html", context)
