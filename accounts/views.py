from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import logout_then_login
from django.http import HttpRequest
from django.shortcuts import render, redirect

# Create your views here.
from .forms import SignupForm


def signout(request:HttpRequest):
    messages.success(request, "로그아웃 되었습니다.")
    return logout_then_login(request)


def signup(request:HttpRequest):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            auth_login(request, signed_user)
            messages.success(request, "회원가입 환영합니다.")

            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })