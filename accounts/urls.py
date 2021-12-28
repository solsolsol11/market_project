from django.urls import path

from accounts import views

urlpatterns = [
    path('signup/', views.signup),
    path('signout/', views.signout),
    path('signin/', views.signin),
]