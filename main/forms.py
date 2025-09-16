# main/forms.py
from django import forms
from main.models import Product

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "brand",
            "price",
            "description",
            "thumbnail",
            "category",
            "stock",
            "is_featured",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Product name"}),
            "brand": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "thumbnail": forms.URLInput(attrs={"class": "form-control", "placeholder": "https://..."}),
            "category": forms.TextInput(attrs={"class": "form-control"}),
            "stock": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            "is_featured": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
