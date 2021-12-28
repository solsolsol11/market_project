from django.urls import path

from products import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name ='list'),
    path('<int:product_id>/', views.product_detail, name ='detail'),
    path('<int:product_id>/question/create', views.question_create, name ='question_create'),
    path('<int:product_id>/question/delete/<int:question_id>', views.question_delete, name ='question_delete'),
    path('<int:product_id>/question/modify/<int:question_id>', views.question_modify, name ='question_modify'),

]