from django.urls import path
from . import views
from articles import views as art_views

urlpatterns = [
    path('dashboard', art_views.dashboard),
    path('dashboard/<int:year>', art_views.dashboard),
    path('<int:id>', art_views.article_by_id),
    path('tag/<str:tag>', art_views.articles_by_tag),
]
