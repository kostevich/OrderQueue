from django.shortcuts import render
from Source.Functions import *
from Source.Menu import *
from Source.Order import *

import os

path = "C:\Data storage\Programming\Internship\OrderQueue\OrderQueue\json"


def MainPage(request):
    if os.path.exists(path + "/InfoOrders.json"):
        InfoOrders = InfoOrdersRead()
    else:
        InfoOrders = {"Id": 0,
                      "User": { 
                          "Name": "", 
                          "Adress": "",
                          "PhoneNumber": 0
                          },
                    "TotalPrice": "",
                    "Datetime": "",
                    "Pizzas": []}
        
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
        # Если ничего не добавлено в корзину.
        if len(InfoOrders["Pizzas"]) == 0:
            # Общая цена всех пицц в корзине.
            InfoOrders["TotalPrice"] = int(request.POST["Count"]) * float(request.POST["Price"])
            # Добавить данные о пицце в корзине.
            InfoOrders["Pizzas"].append({"Id": int(request.POST["Id"]),
                                    "Name": request.POST["Name"],
                                    "Price": float(request.POST["Price"]),
                                    "Count": int(request.POST["Count"])})
            
        # Если в корзине что-то есть.
        else:
            # Количество словарей в списке корзины.
            for i in range(len(InfoOrders["Pizzas"])):
                # Если id пиццы совпадает с id имеющегося словаря.
                if request.POST["Id"] in str(InfoOrders["Pizzas"][i]["Id"]):
                    # Изменяем количество однотипных пицц в корзине.
                    InfoOrders["Pizzas"][i]["Count"] = InfoOrders["Pizzas"][i]["Count"]+int(request.POST["Count"])
                    # Выйти из цикла.
                    break


            else:
                # Добавить данные о пицце в корзине.
                InfoOrders["Pizzas"].append({"Id": int(request.POST["Id"]),
                                "Name": request.POST["Name"],
                                "Price": float(request.POST["Price"]),
                                "Count": int(request.POST["Count"])})
                
        # Если в корзине что-то есть.
        if len(InfoOrders["Pizzas"]) != 0:
            # Обнуление словаря.
            InfoOrders["TotalPrice"] = 0
            # Количество словарей в списке корзины.
            for i in range(len(InfoOrders["Pizzas"])):
                # Расчет общей цены в корзине.
                InfoOrders["TotalPrice"] += InfoOrders["Pizzas"][i]["Price"] * InfoOrders["Pizzas"][i]["Count"]
            InfoOrders["TotalPrice"] = round(InfoOrders["TotalPrice"], 2)


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
            for i in range(len(InfoOrders["Pizzas"])):
                if InfoOrders["Pizzas"][i]["Id"] == int(request.POST["Id"]) and InfoOrders["Pizzas"][i]["Count"] == int(request.POST["Count"]):
                    InfoOrders["TotalPrice"] = round(InfoOrders["TotalPrice"] - InfoOrders["Pizzas"][i]["Price"]*float(request.POST["Count"]), 2)
                    del InfoOrders["Pizzas"][i]
                    break
                elif InfoOrders["Pizzas"][i]["Id"] == int(request.POST["Id"]):
                    InfoOrders["TotalPrice"] = round(InfoOrders["TotalPrice"] - InfoOrders["Pizzas"][i]["Price"]*float(request.POST["Count"]), 2)
                    InfoOrders["Pizzas"][i]["Count"] = InfoOrders["Pizzas"][i]["Count"] - int(request.POST["Count"])
                    break
                else:
                    pass

            InfoOrdersWrite(InfoOrders)     

               
    # Отображение контента на странице.
    context = {"Pizzas": InfoOrders["Pizzas"], "TotalPrice": InfoOrders }

    # Вывод данных на главной странице.
    return render(request, "preorder.html", context)


def FormPage(request):
    InfoOrders = InfoOrdersRead()
    if request.method =="POST":
        if str(request.POST["button"]) == "Оформить заказ":
            pass
        
    InfoOrdersWrite(InfoOrders)     

    # Отображение контента на странице.
    context = {"Pizzas": InfoOrders["Pizzas"], "TotalPrice": InfoOrders }

    return render(request, "form.html", context)