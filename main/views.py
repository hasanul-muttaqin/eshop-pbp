from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductsForm
import uuid

def main_view(request):
    products = Product.objects.all()
    return render(request, "main.html", {"products": products})

def create_products(request):
    form = ProductsForm(request.POST or None)  # no request.FILES needed for URLField

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:main_view")   # sends user back to main list

    return render(request, "create_products.html", {"form": form})

def show_products(request, id):  # singular: detail view
    product = get_object_or_404(Product, pk=id)
    return render(request, "show_products.html", {"product": product})
