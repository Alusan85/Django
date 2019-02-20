from django.urls import path
from .views import (
    product_list_view, product_detail_view,
    products_cat, products_category,
)

urlpatterns = [
    path('', product_list_view, name='list'),
    path('<int:pk>/', product_detail_view, name='detail'),
    path('cat/', products_cat, name='product_cat'),
    path('products_category/', products_category, name='products_category'),
    
]
