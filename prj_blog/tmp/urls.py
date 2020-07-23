from django.urls import path  # из библиотеки django.urls импортируем функцию path
from . import views  # импортируем файл views.py из корня проекта

urlpatterns = [
    path('', views.index)
]