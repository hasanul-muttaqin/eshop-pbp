from django.shortcuts import render
from .models import Product

def main_view(request):
    # ambil satu produk pertama (untuk demo/hw cukup)
    product = Product.objects.first()
    return render(request, "main.html", {"product": product})
