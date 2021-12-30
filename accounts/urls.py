from django.urls import path

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('signin/', views.signin, name='signin'),
    path('find_username/', views.find_username, name='find_username'),
    path('signin/kakao/', views.kakao_login, name='kakao_signin'),
    path('signin/kakao/callback/', views.kakao_signin_callback, name='kakao_signin_callback'),
]
