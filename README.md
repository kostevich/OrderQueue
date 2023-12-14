# OrderQueue
**OrderQueue** – cайт пиццерии на [Django](https://www.djangoproject.com/), отображающий удобный для персонала процесс готовки пиццы.

# Порядок установки и использования
1. Загрузить репозиторий. Распаковать. (Если релиза нет)
2. Установить [Python](https://www.python.org/downloads/) версии не старше 3.11. Рекомендуется добавить в PATH.
3. В среду исполнения установить следующие пакеты: [beautifulsoup4](https://github.com/wention/BeautifulSoup4?ysclid=lq5iqf7qlk644874209), [celery](https://github.com/celery/celery?ysclid=lq5irp37ze849199778), [Django](https://github.com/django/django?ysclid=lph3fmn0za256973455), [dublib](https://github.com/DUB1401/dublib), [requests](https://github.com/psf/requests?ysclid=lpz9y7goms697626558). 
```
pip install beautifulsoup4
pip install celery
pip install Django
pip install git+https://github.com/DUB1401/dublib
pip install requests
```
Либо установить сразу все пакеты при помощи следующей команды, выполненной из директории скрипта.
```
pip install -r requirements.txt
```
4. В среде исполнения запустить файл _manage.py_ командой:

```
python manage.py runserver
```
5. Перейти по ссылке (пример: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)).

# Отслеживание данных в административной панели Django.

1. В среде исполнения запустить команду:

```
python manage.py createsuperuser
```
2. Зарегистрироваться.
3. Перейти по ссылке добавив к ней admin (пример: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)).

# Отслеживание в базе данных.

Откройте файл db.sqlite3 в программе для открытия баз данных (пример: [SQLiteStudio](https://sqlitestudio.pl/)).

# Пример работы

**Главная страница сайта:**

![image](https://github.com/kostevich/WeatherTracking/assets/109979502/8e13e3a5-b068-4588-b29d-e83f02e363df)

**Корзина:**

![image](https://github.com/kostevich/WeatherTracking/assets/109979502/cfe4eb8d-fe2c-4cb3-8d4f-9b285af94a08)

**Оформление заказа:**

![image](https://github.com/kostevich/WeatherTracking/assets/109979502/fc7590ae-8f5f-4cb6-9102-683b1b7f5c32)

**Результат оформления заказа:**

![image](https://github.com/kostevich/WeatherTracking/assets/109979502/55347c67-b0b5-4505-8921-2e38ff0e286b)

_Copyright © Kostevich Irina. 2023._
