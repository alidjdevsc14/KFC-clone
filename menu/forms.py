from django import forms
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
        # exclude = ['created_at']
