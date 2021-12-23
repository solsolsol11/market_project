
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from products.models import Product


def product_list(request: HttpRequest):
    products = Product.objects.order_by('-id')

    return render(request, "products/product_list.html", {
        "products": products
    })

def product_detail(request: HttpRequest, id):
    product = get_object_or_404(Product, id=id)

    product_reals = product.product_reals.order_by('option_1_display_name', 'option_2_display_name')


    return render(request, "products/product_detail.html", {
        "product": product,
        "product_reals": product_reals,
    })