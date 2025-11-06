from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock', 'talla', 'color')
    list_filter = ('categoria', 'talla', 'color')
    search_fields = ('nombre', 'descripcion')