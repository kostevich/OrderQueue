from dublib.Methods import ReadJSON, WriteJSON

# Запись словаря меню в JSON.
def InfoPizzasWrite(InfoPizzas):
    WriteJSON('json/InfoPizzas.json', InfoPizzas)

# Запись словаря корзины в JSON.
def InfoOrdersWrite(InfoOrders):
    WriteJSON('json/InfoOrders.json', InfoOrders)

# Чтение словаря меню в JSON.
def InfoPizzasRead():
    InfoPizzas = ReadJSON('json\InfoPizzas.json')
    return InfoPizzas

# Чтение словаря корзины в JSON.
def InfoOrdersRead():
    InfoOrders = ReadJSON('json\InfoOrders.json')
    return InfoOrders




    