# main/forms.py
from django import forms
from main.models import Product

# Define choices at module level so Meta can reference them safely
CATEGORY_CHOICES = [
    ("ball", "Ball"),
    ("jersey", "Jersey"),
    ("shoes", "Shoes"),
    ("socks", "Socks"),
    ("shin_guards", "Shin Guards"),
    ("goalkeeper_gloves", "Goalkeeper Gloves"),
    ("training_equipment", "Training Equipment"),
    ("bag", "Bag"),
    ("accessories", "Accessories"),
    ("other", "Other"),
]

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
            "brand": forms.TextInput(attrs={"class": "form-control", "placeholder": "Product brand"}),
            "price": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "desc..."}),
            "thumbnail": forms.URLInput(attrs={"class": "form-control", "placeholder": "https://..."}),
            "category": forms.Select(choices=CATEGORY_CHOICES, attrs={"class": "form-control"}),
            "stock": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            "is_featured": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
