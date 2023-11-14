from django.db import models

# Create your models here.

class Order(models.Model):
    Time = models.DateTimeField()
    IdOrder = models.IntegerField()
    NameUser = models.TextField(max_length=100)
    Adress = models.TextField(max_length=100)
    PhoneNumber = models.TextField(max_length=25)
    TotalPrice = models.FloatField()
    NamePizza = models.TextField(max_length=25)
    Count = models.IntegerField()

    def __str__(self):
        return str(self.IdOrder)

    class Meta():
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"





