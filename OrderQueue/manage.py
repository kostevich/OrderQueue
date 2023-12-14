#!/usr/bin/env python

#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from dublib.Methods import CheckPythonMinimalVersion


import os
import sys

#==========================================================================================#
# >>>>> ИНИЦИАЛИЗАЦИЯ СКРИПТА <<<<< #
#==========================================================================================#

def main():
    # Проверка настроек
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OrderQueue.settings')
    # Проверка импорта Django.
    try:
        # Удаление ненужных файлов json.
        os.remove('C:\Data storage\Programming\Internship\OrderQueue\OrderQueue\json\InfoPizzas.json')
        os.remove('C:\Data storage\Programming\Internship\OrderQueue\OrderQueue\json\InfoOrders.json')
    except:
        pass
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    # Проверка поддержки используемой версии Python.
    CheckPythonMinimalVersion(3, 11)


if __name__ == '__main__':
    main()
