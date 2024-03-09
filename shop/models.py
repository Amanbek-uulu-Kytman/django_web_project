from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return f'Элемент {self.name} цена {self.price} '


class Purchase(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date_purchase = models.DateTimeField()

    def __str__(self):
        return f'Покупка Название {self.name} дата {self.age} дата покупки{self.date_purchase}'
