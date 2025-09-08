import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    name = models.CharField(max_length=255)  # Nama item
    brand = models.CharField(max_length=100, default="")  # Brand/merk produk
    price = models.PositiveIntegerField()  # Harga item (Rp)
    description = models.TextField()  # Deskripsi item
    thumbnail = models.URLField(blank=True, null=True)  # Gambar produk
    category = models.CharField(max_length=100)  # Kategori produk
    stock = models.PositiveIntegerField(default=0)  # Jumlah stok
    is_featured = models.BooleanField(default=False)  # Status unggulan

    created_at = models.DateTimeField(auto_now_add=True)  # otomatis isi saat dibuat
    updated_at = models.DateTimeField(auto_now=True)  # otomatis update setiap save()

    def __str__(self):
        return f"{self.name} ({self.brand})"

    @property
    def is_in_stock(self):
        return self.stock > 0
