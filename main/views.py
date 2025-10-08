from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductsForm
import uuid
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

@login_required(login_url='/login')
def main_view(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'
    if filter_type == "all":
        products = Product.objects.all()
    else:
        products = Product.objects.filter(user=request.user)
    user = request.user
    cookies = request.COOKIES.get('last_login', 'Never')
    context = {
        "products": products,
        "last_login": cookies,
        "filter": filter_type,
        "user": user}
    return render(request, "main.html", context)

def create_products(request):
    form = ProductsForm(request.POST or None) 

    if request.method == "POST" and form.is_valid():
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect("main:main_view")

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
     products_list = Product.objects.select_related('user').all()
     data = [
         {
             'id': str(p.id),
             'name': p.name,
             'brand': p.brand,
             'price': p.price,
             'description': p.description,
             'thumbnail': p.thumbnail,
             'category': p.category,
             'stock': p.stock,
             'is_featured': p.is_featured,
             'created_at': p.created_at.isoformat() if p.created_at else None,
             'updated_at': p.updated_at.isoformat() if p.updated_at else None,
             'user_id': p.user_id,
             'user_username': p.user.username if p.user_id else None,
         }
         for p in products_list
     ]
     return JsonResponse(data, safe=False)

def show_xml_by_id(request, products_id):
    try:
        product = Product.objects.filter(pk=products_id)
        xml_data = serializers.serialize("xml", product)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
def show_json_by_id(request, products_id):
    try:
        p = Product.objects.select_related('user').get(pk=products_id)
        data = {
            'id': str(p.id),
            'name': p.name,
            'brand': p.brand,
            'price': p.price,
            'description': p.description,
            'thumbnail': p.thumbnail,
            'category': p.category,
            'stock': p.stock,
            'is_featured': p.is_featured,
            'created_at': p.created_at.isoformat() if p.created_at else None,
            'updated_at': p.updated_at.isoformat() if p.updated_at else None,
            'user_id': p.user_id,
            'user_username': p.user.username if p.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'redirect_url': reverse('main:login'),
                    'message': 'Your account has been successfully created!'
                })
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                response = JsonResponse({
                    'success': True,
                    'redirect_url': reverse('main:main_view')
                })
            else:
                response = HttpResponseRedirect(reverse("main:main_view"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(f"{reverse('main:login')}?logged_out=1")
    response.delete_cookie('last_login')
    return response

def delete_products(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:main_view'))


def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductsForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:main_view')

    context = {
        'form': form
    }

    return render(request, "edit_products.html", context)

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name", ""))
    brand = strip_tags(request.POST.get("brand", ""))
    description = strip_tags(request.POST.get("description", ""))
    category = strip_tags(request.POST.get("category", ""))
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'

    try:
        price = int(request.POST.get("price", 0))
    except ValueError:
        price = 0

    try:
        stock = int(request.POST.get("stock", 0))
    except ValueError:
        stock = 0

    product = Product(
        name=name,
        brand=brand,
        price=price,
        description=description,
        thumbnail=thumbnail,
        category=category,
        stock=stock,
        is_featured=is_featured,
        user=request.user if request.user.is_authenticated else None,
    )
    product.save()
    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@require_POST
def update_product_entry_ajax(request, id):
    product = get_object_or_404(Product, pk=id)

    name = strip_tags(request.POST.get("name", product.name))
    brand = strip_tags(request.POST.get("brand", product.brand))
    description = strip_tags(request.POST.get("description", product.description))
    category = strip_tags(request.POST.get("category", product.category))
    thumbnail = request.POST.get("thumbnail", product.thumbnail)
    is_featured = request.POST.get("is_featured") == 'on' if 'is_featured' in request.POST else product.is_featured

    try:
        price = int(request.POST.get("price", product.price))
    except ValueError:
        price = product.price

    try:
        stock = int(request.POST.get("stock", product.stock))
    except ValueError:
        stock = product.stock

    product.name = name
    product.brand = brand
    product.price = price
    product.description = description
    product.thumbnail = thumbnail
    product.category = category
    product.stock = stock
    product.is_featured = is_featured
    product.save()

    return HttpResponse(b"UPDATED", status=200)

@csrf_exempt
@require_POST
def delete_product_entry_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponse(b"DELETED", status=200)
