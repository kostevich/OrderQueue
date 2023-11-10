from django.shortcuts import render
from Source.Functions import *
from Source.Menu import *
from Source.Order import *

import os
import datetime

path = "C:\Data storage\Programming\Internship\OrderQueue\OrderQueue\json"


def MainPage(request):
    if os.path.exists(path + "/InfoOrders.json"):
        InfoOrders = InfoOrdersRead()
    else:
        InfoOrders = {"LastId": 0,
                      "Queue": [],
                      "Orders": [{"Id": 0,
                      "User": [],
                    "TotalPrice": "",
                    "Datetime": "",
                    "Pizzas": []}]}
        
        InfoOrdersWrite(InfoOrders)


    if os.path.exists(path + "/InfoPizzas.json"):  
        InfoPizzas = InfoPizzasRead()
    else:
        InfoPizzas = ReceiveMenu()
        InfoPizzasWrite(InfoPizzas)
        

    # Словарь добавления в корзину.
    AddOrder = {"Id": 0, "Text": ""}
    
    # Если нажата кнопка в корзину и количество выбранных пицц больше 0.
    if request.method =="POST" and int(request.POST["Count"])>0:
        for Order in range(len(InfoOrders["Orders"])):
            # Если ничего не добавлено в корзину.
            if len(InfoOrders["Orders"][Order]["Pizzas"]) == 0:
                # Общая цена всех пицц в корзине.
                InfoOrders["Orders"][Order]["TotalPrice"] = int(request.POST["Count"]) * float(request.POST["Price"])
                # Добавить данные о пицце в корзине.
                InfoOrders["Orders"][Order]["Pizzas"].append({"Id": int(request.POST["Id"]),
                                        "Name": request.POST["Name"],
                                        "Price": float(request.POST["Price"]),
                                        "Count": int(request.POST["Count"])})
            
            # Если в корзине что-то есть.
            else:
                # Количество словарей в списке корзины.
                for i in range(len(InfoOrders["Orders"][Order]["Pizzas"])):
                    # Если id пиццы совпадает с id имеющегося словаря.
                    if request.POST["Id"] in str(InfoOrders["Orders"][Order]["Pizzas"][i]["Id"]):
                        # Изменяем количество однотипных пицц в корзине.
                        InfoOrders["Orders"][Order]["Pizzas"][i]["Count"] = InfoOrders["Orders"][Order]["Pizzas"][i]["Count"]+int(request.POST["Count"])
                        # Выйти из цикла.
                        break


                else:
                    # Добавить данные о пицце в корзине.
                    InfoOrders["Orders"][Order]["Pizzas"].append({"Id": int(request.POST["Id"]),
                                    "Name": request.POST["Name"],
                                    "Price": float(request.POST["Price"]),
                                    "Count": int(request.POST["Count"])})
                
            # Если в корзине что-то есть.
            if len(InfoOrders["Orders"][Order]["Pizzas"]) != 0:
                # Обнуление словаря.
                InfoOrders["Orders"][Order]["TotalPrice"] = 0
                # Количество словарей в списке корзины.
                for i in range(len(InfoOrders["Orders"][Order]["Pizzas"])):
                    # Расчет общей цены в корзине.
                    InfoOrders["Orders"][Order]["TotalPrice"] += InfoOrders["Orders"][Order]["Pizzas"][i]["Price"] * InfoOrders["Orders"][Order]["Pizzas"][i]["Count"]
                InfoOrders["Orders"][Order]["TotalPrice"] = round(InfoOrders["Orders"][Order]["TotalPrice"], 2)


            # Добавляем текст при нажатии на кнопку.
            AddOrder = {"id": int(request.POST["Id"]), "text": "Пицца добавлена в корзину"}


    
    # Отображение контента на странице.
    context = {"InfoPizzas": InfoPizzas["Pizzas"], "AddOrder": AddOrder}
        

    InfoOrdersWrite(InfoOrders)

    RakingOrders(InfoPizzas)
    # Вывод данных на главной странице.
    return render(request, "main.html", context)


def AboutPage(request):
    return render(request, "about.html")


def PreOrderPage(request):
    InfoOrders = InfoOrdersRead()
    if request.method =="POST":
        if str(request.POST["button"]) == "Удалить из корзины":
            for Order in range(len(InfoOrders["Orders"])):
                for i in range(len(InfoOrders["Orders"][Order]["Pizzas"])):
                    if InfoOrders["Orders"][Order]["Pizzas"][i]["Id"] == int(request.POST["Id"]) and InfoOrders["Orders"][Order]["Pizzas"][i]["Count"] == int(request.POST["Count"]):
                        InfoOrders["Orders"][Order]["TotalPrice"] = round(InfoOrders["Orders"][Order]["TotalPrice"] - InfoOrders["Orders"][Order]["Pizzas"][i]["Price"]*float(request.POST["Count"]), 2)
                        del InfoOrders["Orders"][Order]["Pizzas"][i]
                        break
                    elif InfoOrders["Orders"][Order]["Pizzas"][i]["Id"] == int(request.POST["Id"]):
                        InfoOrders["Orders"][Order]["TotalPrice"] = round(InfoOrders["Orders"][Order]["TotalPrice"] - InfoOrders["Orders"][Order]["Pizzas"][i]["Price"]*float(request.POST["Count"]), 2)
                        InfoOrders["Orders"][Order]["Pizzas"][i]["Count"] = InfoOrders["Orders"][Order]["Pizzas"][i]["Count"] - int(request.POST["Count"])
                        break
                    else:
                        pass

            InfoOrdersWrite(InfoOrders)    
               
    # Отображение контента на странице.
    context = {"Pizzas": InfoOrders["Orders"]}

    # Вывод данных на главной странице.
    return render(request, "preorder.html", context)


def FormPage(request):
    SendForm(request)
    return render(request, "form.html")


def SendForm(request):
    InfoOrders = InfoOrdersRead()
    for Order in range(len(InfoOrders["Orders"])):
        if request.method =="POST":
            if str(request.POST["button"]) == "Оформить":
                InfoOrders["Orders"][Order]["User"].append({"Name": request.POST["Name"],
                                        "Adress": request.POST["Adress"],
                                        "PhoneNumber": str(request.POST['PhoneNumber'])})
                InfoOrders["Orders"][Order]["Datetime"] = str(datetime.datetime.now())
                InfoOrders["Orders"][Order]["Id"] = InfoOrders["LastId"] + 1

                if InfoOrders["Orders"][Order]["Id"] >InfoOrders["LastId"]:
                    InfoOrders["Queue"] = InfoOrders["Orders"][Order]
                    InfoOrders["LastId"] = InfoOrders["LastId"] + 1
                    del InfoOrders["Orders"][Order]
        InfoOrdersWrite(InfoOrders)
        

    # Отображение контента на странице.
    context = {"Pizzas": InfoOrders["Orders"]}

    return render(request, "form.html", context)