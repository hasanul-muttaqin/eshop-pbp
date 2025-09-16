from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductsForm
import uuid
from django.http import HttpResponse
from django.core import serializers

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

def show_xml(request):
     products_list = Product.objects.all()
     xml_data = serializers.serialize("xml", products_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
     products_list = Product.objects.all()
     xml_data = serializers.serialize("xml", products_list)
     return HttpResponse(xml_data, content_type="application/json")

def show_xml_by_id(request):
     products_list = Product.objects.all()
     xml_data = serializers.serialize("xml", products_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json_by_id(request):
     products_list = Product.objects.all()
     json_data = serializers.serialize("json", products_list)
     return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, products_id):
    try:
        product = Product.objects.get(pk=products_id)
        xml_data = serializers.serialize("xml", [product])  # wrap in list
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
def show_json_by_id(request, products_id):
    try:
        product = Product.objects.get(pk=products_id)
        json_data = serializers.serialize("json", [product])  # wrap in list
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

