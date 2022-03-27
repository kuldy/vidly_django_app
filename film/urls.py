from django.urls import path
from . import views


urlpatterns = [
    path('films/', views.film_list),
    path('films/<int:id>/', views.film_detail),
    path('genres/', views.genre_list),
    path('genres/<int:id>/', views.genre_detail),
]
