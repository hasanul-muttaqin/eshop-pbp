from django.urls import path
from .views import main_view, create_products, show_products

app_name = "main"

urlpatterns = [
    path("", main_view, name="main_view"),
    path("create-products/", create_products, name="create_products"),
    path("products/<uuid:id>/", show_products, name="show_products"),  # id is UUID
]
