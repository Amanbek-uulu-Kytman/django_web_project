from django.shortcuts import render

from django.http import HttpResponse

def greetings(request):
    return HttpResponse("Добро пожаловать в наш магазин!")