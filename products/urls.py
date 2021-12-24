from django.urls import path

from products import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name ='list'),
    path('<int:id>/', views.product_detail, name ='detail'),
    path('<int:id>/question/create', views.question_create, name ='question_create'),

]