from django.contrib import admin
from .models import Category, Brand

# Register your models here.



class AdminViewBrand(admin.ModelAdmin):

	list_display = ['id', 'name', 'created_at']



class AdminViewCategory(admin.ModelAdmin):

	list_display = ['id', 'weight', 'created_at']


# class AdminViewProduct(admin.ModelAdmin):
	
# 	list_display = ['id','title', 'quantity', 'category', 'brand', 'is_refill', 'created_at']
# 	list_filter = ['category', 'brand', 'is_refill']
# 	search_fields = ['title']


# class AdminViewCylinder(admin.ModelAdmin):

# 	list_display = ['title', 'quantity', 'category', 'brand']
# 	list_filter = ['category', 'brand']
# 	search_fields = ['title']


admin.site.register(Brand, AdminViewBrand)
admin.site.register(Category, AdminViewCategory)
# admin.site.register(Product, AdminViewProduct)
# admin.site.register(Empty_Cylinder, AdminViewCylinder)