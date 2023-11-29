from django.contrib import admin
from .models import Sale, Due
# Register your models here.

class AdminSaleView(admin.ModelAdmin):
	list_display = ['id', 'product', 'customer', 'is_wholesale', 'is_refill', 'created_at']

class AdminDueView(admin.ModelAdmin):
	list_display = ['id', 'sale', 'due_amount', 'is_paid', 'created_at']



admin.site.register(Sale, AdminSaleView)	
admin.site.register(Due, AdminDueView)