from django.db import models

# Create your models here.

class Order(models.Model):
    Time = models.TextField(unique = True, max_length=100)
    IdOrder = models.IntegerField(unique = True)
    NameUser = models.TextField(max_length=100)
    Adress = models.TextField(max_length=100)
    PhoneNumber = models.TextField(max_length=100)
    TotalPrice = models.TextField(max_length=100)
    NamePizza = models.TextField(max_length=100)
    Count = models.IntegerField()
    def __str__(self):
        return self.IdOrder

    class Meta():
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"





