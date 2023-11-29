from django.contrib import admin
from .models import Category, Brand, Supplier

# Register your models here.



class AdminViewBrand(admin.ModelAdmin):

	list_display = ['id', 'name', 'created_at']



class AdminViewCategory(admin.ModelAdmin):

	list_display = ['id', 'weight', 'created_at']


class AdminSupplierView(admin.ModelAdmin):
	list_display = ['id', 'brand', 'contact_name', 'address', 'phone']



admin.site.register(Brand, AdminViewBrand)
admin.site.register(Category, AdminViewCategory)
admin.site.register(Supplier, AdminSupplierView)