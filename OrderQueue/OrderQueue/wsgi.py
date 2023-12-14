#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from django.core.wsgi import get_wsgi_application


import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OrderQueue.settings')

application = get_wsgi_application()
