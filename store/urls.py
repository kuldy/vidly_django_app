from django.urls import path
from . import views


urlpatterns = [
    path('product/', views.ProductList.as_view()),
    path('product/<int:id>/', views.ProductDetail.as_view()),
    path('collection/', views.collection_list),
    path('collection/<int:pk>/', views.collection_detail, name='collection-detail'),
]
