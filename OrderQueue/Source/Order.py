from celery import Celery


app = Celery('myapp', broker='http://127.0.0.1:8000/')


@app.task
def RakingOrders(InfoPizzas):
   pass