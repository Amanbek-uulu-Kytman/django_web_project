from shop.models import Item

item1 = Item(name='Товар 1', price=100)
item1.save()

item2 = Item(name='Товар 2', price=200)
item2.save()

item3 = Item(name='Товар 3', price=300)
item3.save()

item4 = Item(name='Товар 4', price=400)
item4.save()

item5 = Item(name='Товар 5', price=500)
item5.save()

from shop.models import Purchase, Item
from django.utils import timezone
from datetime import timedelta

for i in range(10):
    item = Item.objects.get(id=i%5+1)
    purchase = Purchase(name=f'Покупатель {i+1}', age=20+i, item=item, date_purchase=timezone.now()-timedelta(days=i))
    purchase.save()