from django.urls import path
from . import views

app_name = 'mart'

urlpatterns = [

	path('product/', views.product_view, name='product'),
	path('product/add/', views.add_product, name='add_product'),
	path('product/update/<int:product_id>/', views.update_product, name='update_product'),
	path('product/delete/<int:product_id>/', views.delete_product, name='delete_product'),

]