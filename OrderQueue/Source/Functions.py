from dublib.Methods import ReadJSON, WriteJSON

# Запись словаря меню в JSON.
def InfoPizzasWrite(InfoPizzas):
    WriteJSON('json/InfoPizzas.json', InfoPizzas)

# Запись словаря корзины в JSON.
def InfoOrdersWrite(InfoOrders):
    WriteJSON('json/InfoOrders.json', InfoOrders)

# Чтение словаря меню в JSON.
def InfoPizzasRead():
    InfoPizzas = ReadJSON('C:\Data storage\Programming\Internship\OrderQueue\OrderQueue\json\InfoPizzas.json')
    return InfoPizzas

# Чтение словаря корзины в JSON.
def InfoOrdersRead():
    InfoOrders = ReadJSON('C:\Data storage\Programming\Internship\OrderQueue\OrderQueue\json\InfoOrders.json')
    return InfoOrders




    