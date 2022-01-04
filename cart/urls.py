from django.urls import path

from . import views


app_name = 'cart'

urlpatterns = [
    path('', views.cart_item, name='cart_item'),
    path('add/', views.add, name='add'),
]