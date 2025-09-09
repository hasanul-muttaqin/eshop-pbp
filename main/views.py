from django.shortcuts import render
from .models import Product
import uuid

def main_view(request):
    product, created = Product.objects.get_or_create(
        id=uuid.UUID("00000000-0000-0000-0000-000000000001"),  # fixed UUID so it won't duplicate
        defaults={
            "name": "Liverpool Original Jersey LFC Away 24/25",
            "brand": "Jersey",
            "price": 899000,
            "description": "Jersey Luar Kandang Liverpool Musim 2024/2025 dengan teknologi DRY-FIT agar tetap nyaman beraktivitas",
            "thumbnail": "https://example.com/liverpool-jersey.jpg",  # replace with actual image URL
            "category": "Jersey",
            "stock": 25,
            "is_featured": True,
        }
    )

    return render(request, "main.html", {"product": product})
