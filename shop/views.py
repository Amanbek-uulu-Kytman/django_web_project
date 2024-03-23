from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Item, Purchase


class ItemListView(ListView):
    model = Item
    template_name = 'list_item.html'
    context_object_name = 'items'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'detail_item.html'
    context_object_name = 'item'


def greetings(request):
    return HttpResponse("Добро пожаловать в наш магазин!")


def detail(request, item_id):
    return HttpResponse(f"Вы находитесь на странице для просмотра {item_id} товара")


def results(request, item_id):
    return HttpResponse(f"Фильмы {item_id} ")


def vote(request, item_id):
    return HttpResponse(f"Вы выбираете фильм {item_id}")
