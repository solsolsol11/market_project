from django.forms import Form, ModelForm

from cart.models import CartItem
from products.models import ProductReal


class CartAddForm(ModelForm):
    def __init__(self, *args, **kwargs):
        product_id: int = kwargs['product_id']
        del kwargs['product_id']
        super().__init__(*args, **kwargs)
        self.fields['product_real'].label = "옵션"

        variants = ProductReal.objects.filter(product_id=product_id)
        products = [(i.id, f'{i.option_1_display_name} / {i.option_2_display_name}') for i in variants]

        self.fields['product_real'].choices = products


    class Meta:
        model = CartItem
        fields = ['product_real', 'quantity']