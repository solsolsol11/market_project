from django.forms import Form, ModelForm

from cart.models import ProductCratItem
from products.models import ProductReal


class ProductCartAddForm(ModelForm):
    def __init__(self, *args, **kwargs):
        product_id: int = kwargs['product_id'] if 'product_id' in kwargs.keys() else 0
        if product_id:
            del kwargs['product_id']
        super().__init__(*args, **kwargs)
        self.fields['product_real'].label = "옵션"

        if product_id:
            product_reals = ProductReal.objects.filter(product_id=product_id)
            product_real_choices = [(i.id, f'{i.option_1_display_name} / {i.option_2_display_name}') for i in product_reals]

            self.fields['product_real'].choices = product_real_choices


    class Meta:
        model = ProductCratItem
        fields = ['product_real', 'quantity']