from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [

    path('add/', views.add, name='add'),
]