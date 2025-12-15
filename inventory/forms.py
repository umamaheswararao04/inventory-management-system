from django import forms
from .models import Product, Category, Supplier

class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label="-- Select Category or Add New --"
    )
    supplier = forms.ModelChoiceField(
        queryset=Supplier.objects.all(),
        required=False,
        empty_label="-- Select Supplier or Add New --"
    )

    class Meta:
        model = Product
        fields = ['name', 'category', 'supplier', 'price', 'quantity']
