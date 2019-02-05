from django.urls import path
from . import views

urlpatterns = [
    path('second/', views.second, name ='second'),
    path('first/', views.first, name ='first'),
    path('product/', views.product, name ='product')

]