from django.urls import path
from .views import main_view, create_products, show_products, show_json, show_xml, show_json_by_id, show_xml_by_id
from .views import register, login_user, logout_user, edit_product
from .views import delete_products

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
]
