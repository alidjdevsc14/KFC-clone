from django import forms
from django.forms import RadioSelect

from .models import Item, Category, SubCategory, Orders


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        # exclude = ['created_at']


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = '__all__'
        # exclude = ['created_at']


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['created_at']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'
        widgets = {
            'is_pickup': RadioSelect(),
        }
        # exclude = ['created_at']


# class CheckoutForm(forms.Form):
#     shipping_address = forms.CharField(label='Shipping address', max_length=100)
#     billing_address = forms.CharField(label='Billing address', max_length=100)
#     card_number = forms.CharField(label='Card number', max_length=16)
#     expiry_date = forms.CharField(label='Expiry date', max_length=5)
#     cvv = forms.CharField(label='CVV', max_length=3)
