from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.http import require_POST

from accounts.models import User
from cart.forms import CartAddForm
from cart.models import CartItem
from products.models import ProductReal, Product


@login_required
@require_POST
def add(request):
    if request.method == "POST":
        product_real_id = request.POST.get('product_real')
        product_real = ProductReal.objects.get(id=product_real_id)
        form = CartAddForm(request.POST, product_id=product_real.product_id)

        if form.is_valid():
            cart_item = form.save(commit=False)
            cart_item.user = request.user
            cart_item.save()

            messages.success(request, "장바구니에 추가되었습니다.")
            return redirect('products:detail', 20)


def cart_item(request, product_real):
    product_real_id = request.POST.get('product_real')
    product_real = ProductReal.objects.get(id=product_real_id)
    form = CartAddForm(request.POST, product_id=product_real.product_id)


    return render(request, 'cart/cart_list.html', {
        'product_real_id': product_real_id,
        'product_real': product_real,
        'form': form,
    })
