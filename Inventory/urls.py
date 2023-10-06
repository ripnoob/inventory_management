from django.urls import path
from . import views
app_name = 'inventory'

urlpatterns = [
	path('dashboard/', views.DashBoard, name='dashboard'),
	path('brand/add/', views.AddBrand, name='brand'),
	path('brand/', views.AllBrand, name='all_brand'),
	path('brand/update/<int:brand_id>/', views.UpdateBrand, name='update_brand'),
	path('brand/delete/<int:brand_id>/', views.DeleteBrand, name='delete_brand'),

	path('category/', views.ViewCategory, name='view_category'),
	path('category/add/', views.AddCategory, name='add_category'),
	path('category/delete/<int:category_id>', views.DeleteCategory, name='delete_category'),
	path('category/update/<int:category_id>', views.UpdateCategory, name='update_category'),
]