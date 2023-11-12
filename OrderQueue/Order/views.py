from django.shortcuts import render
from Source.Functions import *
from Source.Menu import *
from Source.Order import *
from django.http import HttpResponseRedirect

import os
import datetime

# Путь к файлам формата json.
path = "json"

# Открытие главной страницы.
def MainPage(request):
	# Если найден файл InfoOrders.json.
	if os.path.exists(path + "/InfoOrders.json"):
		# Перевод данных файла в словарь.
		InfoOrders = InfoOrdersRead()

		if len(InfoOrders["Orders"]) == 0:
			InfoOrders["Orders"].append({
				"Id": 0,
				"User": [],
				"TotalPrice": "",
				"Datetime": "",
				"Pizzas": []
			})

	# Если не найден.
	else: 
		# Создаем словарь.
		InfoOrders = {"LastId": 0,
					  "Queue": [],
					  "Orders":[
						{"Id": 0,
						 "User": [],
						 "TotalPrice": "",
						 "Datetime": "",
						 "Pizzas": []}]}
		# Сохраняем его в виде файла InfoOrders.json.
		InfoOrdersWrite(InfoOrders)

	# Если найден файл InfoPizzas.json.
	if os.path.exists(path + "/InfoPizzas.json"):
		 # Перевод данных файла в словарь.  
		InfoPizzas = InfoPizzasRead()
	# Если не найден.
	else:
		# Создаем словарь c данными с сайта.
		InfoPizzas = ReceiveMenu()
		 # Сохраняем его в виде файла InfoPizzas.json.
		InfoPizzasWrite(InfoPizzas)
		

	# Словарь добавления в корзину.
	AddOrder = {"Id": 0, "Text": ""}
	
	# Если нажата кнопка в корзину и количество выбранных пицц больше 0.
	if request.method =="POST" and int(request.POST["Count"])>0:
		# Узнаем количество объектов в словаре InfoOrders.
		for Order in range(len(InfoOrders["Orders"])):
			# Если пицц нет в корзине.
			if len(InfoOrders["Orders"][Order]["Pizzas"]) == 0:
				# Общая цена всех пицц в корзине.
				InfoOrders["Orders"][Order]["TotalPrice"] = int(request.POST["Count"]) * float(request.POST["Price"])
				# Добавить данные о пицце в корзине.
				InfoOrders["Orders"][Order]["Pizzas"].append({"Id": int(request.POST["Id"]),
										"Name": request.POST["Name"],
										"Price": float(request.POST["Price"]),
										"Count": int(request.POST["Count"])})
			
			# Если в корзине есть пицца с таким же названием.
			else:
				# Узнаем количество наименований пицц в корзине.
				for i in range(len(InfoOrders["Orders"][Order]["Pizzas"])):
					# Если id пиццы совпадает с id имеющегося словаря.
					if request.POST["Id"] in str(InfoOrders["Orders"][Order]["Pizzas"][i]["Id"]):
						# Изменяем количество однотипных пицц в корзине.
						InfoOrders["Orders"][Order]["Pizzas"][i]["Count"] += int(request.POST["Count"])
						# Выйти из цикла.
						break


				else:
				# Если в корзине нет идентичной пиццы - добавляем информацию о ней .
					InfoOrders["Orders"][Order]["Pizzas"].append({"Id": int(request.POST["Id"]),
										"Name": request.POST["Name"],
										"Price": float(request.POST["Price"]),
										"Count": int(request.POST["Count"])})
				
			# Добавление общей стоимости пицц.
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
		
	# Сохраняем данные в виде файла InfoOrders.json.
	InfoOrdersWrite(InfoOrders)
	# Сохраняем данные в виде файла InfoPizzas.json.
	RakingOrders(InfoPizzas)
	# Вывод данных на главной странице.
	return render(request, "main.html", context)


def AboutPage(request):
	return render(request, "about.html")


def PreOrderPage(request):
	# Перевод данных файла в словарь.
	InfoOrders = InfoOrdersRead()
	print(1, InfoOrders)
	# Если пришёл POST - запрос.
	if request.method =="POST":
		# Нажата кнопка: Удалить из корзины.
		if str(request.POST["button"]) == "Удалить из корзины":
			# Узнаем количество объектов в словаре InfoOrders["Orders"].
			for Order in range(len(InfoOrders["Orders"])):
				# Узнаем количество объектов в словаре InfoOrders["Orders"][Order]["Pizzas"].
				for i in range(len(InfoOrders["Orders"][Order]["Pizzas"])):
					# Если id пиццы, которую нужно удалить такое же, и количество совпадает. 
					if InfoOrders["Orders"][Order]["Pizzas"][i]["Id"] == int(request.POST["Id"]) and InfoOrders["Orders"][Order]["Pizzas"][i]["Count"] == int(request.POST["Count"]):
						# Узнаем общую стоимость пиццы и сохраняем.
						InfoOrders["Orders"][Order]["TotalPrice"] += round(InfoOrders["Orders"][Order]["TotalPrice"] - InfoOrders["Orders"][Order]["Pizzas"][i]["Price"]*float(request.POST["Count"]), 2)
						# Удаление ненужной пиццы.
						del InfoOrders["Orders"][Order]["Pizzas"][i]
						break
					# # Если id пиццы, которую нужно удалить такое же.
					elif InfoOrders["Orders"][Order]["Pizzas"][i]["Id"] == int(request.POST["Id"]):
						# Меняем общую стоимость.
						InfoOrders["Orders"][Order]["TotalPrice"] = round(InfoOrders["Orders"][Order]["TotalPrice"] - InfoOrders["Orders"][Order]["Pizzas"][i]["Price"]*float(request.POST["Count"]), 2)
						# Меняем количество пицц в корзине.
						InfoOrders["Orders"][Order]["Pizzas"][i]["Count"] = InfoOrders["Orders"][Order]["Pizzas"][i]["Count"] - int(request.POST["Count"])
						break

	# Сохраняем данные в виде файла InfoOrders.json.
	InfoOrdersWrite(InfoOrders)    
			
	# Отображение контента на странице.
	context = {"Pizzas": InfoOrders["Orders"]}

	# Вывод данных на главной странице.
	return render(request, "preorder.html", context)

# Если попали на страницу формы.
def FormPage(request):
	# Перевод данных файла в словарь.
	InfoOrders = InfoOrdersRead()
	for Order in range(len(InfoOrders["Orders"])):
		if request.method =="POST":
			if request.POST["button"] == "Оформить":
				InfoOrders["Orders"][Order]["User"].append({"Name": request.POST["Name"],
										"Adress": request.POST["Adress"],
										"PhoneNumber": str(request.POST['PhoneNumber'])})
				InfoOrders["Orders"][Order]["Datetime"] = str(datetime.datetime.now())
				InfoOrders["Orders"][Order]["Id"] = InfoOrders["LastId"] + 1
				InfoOrders["LastId"] += 1
				InfoOrders["Queue"].append(InfoOrders["Orders"][Order])
				InfoOrders["Orders"] = list()
				InfoOrdersWrite(InfoOrders)
				return HttpResponseRedirect("/orders")  

	return render(request, "form.html")
   
	
def SendForm(request):
	return render(request, "orders.html")