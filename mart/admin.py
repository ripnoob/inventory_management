from django.contrib import admin
from .models import Product
# Register your models here.

class AdminProductView(admin.ModelAdmin):
	list_display = ['id','title', 'brand', 'category', 'price', 'quantity', 'created_at']

admin.site.register(Product, AdminProductView)