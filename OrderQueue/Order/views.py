from django.shortcuts import render
from dublib.Methods import ReadJSON, WriteJSON
from Source.Menu import InfoPizzas

# Создание словаря товаров, находящегося в корзине.
InfoOrders = {
    'Orders': []
}


def MainPage(request):
    # Словарь добавления в корзину.
    AddOrder = {'id': "0", 'text': ''}
    AllPrice = {'AllPrice': '0 руб.' }

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
    
    # Создание json файликов с данными.
    WriteJSON('InfoOrders.json', InfoOrders)
    WriteJSON('AllPrice.json', AllPrice)

    # Вывод данных на главной странице.
    return render(request, "main.html", context)


def AboutPage(request):
    return render(request, "about.html")


def PreOrderPage(request):
    # Создание словарей из json файликов с данными.
    InfoOrdersDict = ReadJSON('C:\Data storage\Programming\Internship\OrderQueue\OrderQueue\InfoOrders.json')
    AllPriceDict = ReadJSON('C:\Data storage\Programming\Internship\OrderQueue\OrderQueue\AllPrice.json')

    # Отображение контента на странице.
    context = {'InfoOrdersDict': InfoOrdersDict["Orders"],'AllPriceDict': AllPriceDict}

    # Вывод данных на главной странице.
    return render(request, "preorder.html", context)
