from django.urls import path

from . import views


app_name = 'cart'

urlpatterns = [
    path('', views.my_cart, name='my_cart'),
    path('add/', views.add, name='add'),
]