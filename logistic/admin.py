from django.contrib import admin
from .models import Product, Stock


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass
