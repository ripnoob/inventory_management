from django.urls import path
from . import views

app_name = 'mart'

urlpatterns = [

	path('product/', views.product_view, name='product'),
	path('product/add/', views.add_product, name='add_product'),
	path('product/update/<int:product_id>/', views.update_product, name='update_product'),
	path('product/delete/<int:product_id>/', views.delete_product, name='delete_product'),

	path('add/purchase', views.add_purchase, name='add_purchase'),
	path('purchase/all/', views.view_purchase, name='view_purchase'),
	path('delete/purchase/<int:purchase_id>/', views.delete_purchase, name='delete_purchase'),
	path('update/purchase/<int:purchase_id>/', views.update_purchase, name='update_purchase'),

	path('add/return/', views.add_return, name='add_return'),
	path('return/all/', views.view_return, name='view_return'),
	path('return/update/<int:return_id>/', views.update_return, name='update_return'),
	path('return/delete/<int:return_id>/', views.delete_return, name='delete_return'),

]