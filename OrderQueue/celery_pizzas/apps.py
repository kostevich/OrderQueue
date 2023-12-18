
#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from django.apps import AppConfig


class CeleryPizzasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'celery_pizzas'
