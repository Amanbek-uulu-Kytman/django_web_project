from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Item, Purchase


def list_item(request):
    items = Item.objects.filter()
    context = {
        "items": items,
    }
    return render(request, "list_item.html", context)


def detail_item(request, id):
    item = Item.objects.get(id=id)
    purchases = item.purchase_set.all()
    context = {
        "item": item,
        "purchases": purchases
        }
    return render(request, "detail_item.html", context)


def greetings(request):
    return HttpResponse("Добро пожаловать в наш магазин!")


def detail(request, item_id):
    return HttpResponse(f"Вы находитесь на странице для просмотра {item_id} товара")


def results(request, item_id):
    return HttpResponse(f"Фильмы {item_id} ")


def vote(request, item_id):
    return HttpResponse(f"Вы выбираете фильм {item_id}")
