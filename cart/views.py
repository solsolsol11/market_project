from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.




def cart_view(request: HttpRequest):
    return HttpResponse("장바구니")
