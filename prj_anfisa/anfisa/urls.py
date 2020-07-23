from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about),
    path('', views.index)
    # здесь надо добавить path() для главной страницы
]