from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductsForm
import uuid
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/login')
def main_view(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'
    if filter_type == "all":
        products = Product.objects.all()
    else:
        products = Product.objects.filter(user=request.user)
    user = request.user
    cookies = request.COOKIES.get('last_login', 'Never')
    return render(request, "main.html", {"products": products, "last_login": cookies, "filter": filter_type, "user": user})

def create_products(request):
    form = ProductsForm(request.POST or None)  # no request.FILES needed for URLField

    if request.method == "POST" and form.is_valid():
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect("main:main_view")   # sends user back to main list

    return render(request, "create_products.html", {"form": form})

@login_required(login_url='/login')
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
    
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:main_view"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response


   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

