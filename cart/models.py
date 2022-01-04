from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from accounts.models import User
from products.models import ProductReal, Product




class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    reg_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_real = models.ForeignKey(ProductReal, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField('수량', default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product



