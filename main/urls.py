from django.urls import path
from .views import (
    main_view,
    create_products,
    show_products,
    show_json,
    show_xml,
    show_json_by_id,
    show_xml_by_id,
    register,
    login_user,
    logout_user,
    edit_product,
    delete_products,
    add_product_entry_ajax,
    update_product_entry_ajax,
    delete_product_entry_ajax,
)

app_name = "main"

urlpatterns = [
    path("", main_view, name="main_view"),
    path("create-products/", create_products, name="create_products"),
    path("products/<uuid:id>/", show_products, name="show_products"),  # id is UUID\
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:products_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:products_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path("products/<uuid:id>/edit", edit_product, name= 'edit_product'),
    path("products/<uuid:id>/delete", delete_products, name= 'delete_products'),
    path('create-products-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('products/<uuid:id>/update-ajax', update_product_entry_ajax, name='update_product_entry_ajax'),
    path('products/<uuid:id>/delete-ajax', delete_product_entry_ajax, name='delete_product_entry_ajax'),
]
