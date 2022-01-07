from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.core import exceptions

# Create your views here.
from django.views.decorators.http import require_POST

from accounts.models import User
from cart.forms import ProductCartAddForm
from cart.models import ProductCratItem
from products.models import ProductReal, Product


@login_required
@require_POST
def add(request):


        product_real:ProductReal = ProductReal.objects.get(id=request.POST.get('product_real'))
        form = ProductCartAddForm(request.POST)

        if form.is_valid():
            cart_item = form.save(commit=False)
            cart_item.user = request.user
            cart_item.save()

            messages.success(request, "장바구니에 추가되었습니다.")
            return redirect('products:detail', product_real.product_id)

        messages.error(request, form['quantity'].errors, 'danger')
        return redirect('products:detail', product_real.product.id)


@login_required
def cart_item(request):
    cart_items = ProductCratItem.objects.filter(user=request.user)

    return render(request, 'cart/cart_list.html', {
        'cart_items': cart_items
    })

@login_required
def cart_delete(request:HttpRequest):
    cart_items = ProductCratItem.objects.filter(user=request.user)


    cart_items.delete()


    messages.success(request, "상품이 삭제되었습니다")

    return redirect("/cart")
