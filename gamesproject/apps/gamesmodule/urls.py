from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('index/list_games/', views.list_games, name='games.list_games')
]
