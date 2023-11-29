from django.contrib import admin
from .models import Product, Purchase, EmptySylinder, Return
# Register your models here.

class AdminProductView(admin.ModelAdmin):
	list_display = ['id','title', 'brand', 'category', 'price', 'quantity', 'created_at']


class AdminPurchaseView(admin.ModelAdmin):
	list_display = ['id', 'product', 'supplier', 'quantity', 'cost', 'extra_cost', 'is_refill', 'created_at']
	list_filter = ['is_refill', 'product']
	list_editable = ['is_refill']

class AdminEmptySylinderView(admin.ModelAdmin):
	list_display = ['id', 'product', 'brand', 'category', 'quantity', 'created_at']


class AdminReturnView(admin.ModelAdmin):
	list_display = ['id', 'purchase', 'quantity', 'return_cost', 'issue', 'created_at']







admin.site.register(Product, AdminProductView)
admin.site.register(Purchase, AdminPurchaseView)
admin.site.register(EmptySylinder, AdminEmptySylinderView)
admin.site.register(Return, AdminReturnView)
