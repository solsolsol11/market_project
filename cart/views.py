from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect

# Create your views here.
from accounts.models import User
from cart.forms import CartAddForm
from cart.models import CartItem
from products.models import ProductReal, Product


@login_required
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

def add_cart(request, product_pk):
    product = Product.objects.get(pk=product_pk)

    try:
        cart = CartItem.objects.get(product_id=product.pk, user_id=request.user.pk)
        if cart:
            if cart.product.name == product.name:
                cart.quantity += 1
                cart.save()
    except CartItem.DoesNotExist:
        user = User.objects.get(pk=request.user.pk)
        cart = CartItem(
            user=user,
            product=product,
            quantity=1,
        )
        cart.save()
    return redirect('product:my-cart')




def my_cart(request):

    cart_item = CartItem.objects.filter(user_id=request.user.pk)
    total_price = 0
    for each_total in cart_item:
        total_price += each_total.product.sale_price * each_total.quantity
    if cart_item is not None:
        context = {
            'cart_item': cart_item,
            'total_price':total_price,
        }
        return render(request, 'cart/cart_list.html', context)
    return redirect('product:my-cart')

def minus_cart_item(request, product_pk):
    cart_item = CartItem.objects.filter(product_id=product_pk)
    product = Product.objects.get(pk=product_pk)
    try:
        for item in cart_item:
            if item.product.name == product.name:
                if item.quantity > 1:
                    item.quantity -= 1
                    item.save()
                return redirect('product:my-cart')
            else:
                return redirect('product:my-cart')
    except CartItem.DoesNotExist:
        raise Http404





