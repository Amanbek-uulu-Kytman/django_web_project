from django.urls import path
from .views import greetings, detail, results, vote, list_item, detail_item

urlpatterns = [
    path('shop', list_item, name='list_item'),
    path('shop/<int:id>/', detail_item, name='detail_item'),
    path('shop/greetings', greetings, name="greetings"),
    path('shop/greetings/<int:film_id>/', detail, name="detail"),
    path('shop/greetings/<int:film_id>/results', results, name="results"),
    path('shop/greetings/<int:film_id>/vote', vote, name="vote"),

]
