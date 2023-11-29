from django.urls import path
from . import views


app_name = 'gross'

urlpatterns = [
		
		path('sale/add/', views.AddSale, name='add_sale'),
		path('sale/view/', views.ViewSale, name='view_sale'),
		path('sale/update/<int:sale_id>/', views.UpdateSale, name='update_sale'),
		path('sale/delete/<int:sale_id>/', views.DeleteSale, name='delete_sale'),

		path('due/view/', views.ViewDue, name='view_due'),
		path('due/add/', views.AddDue, name='add_due'),
		path('due/update/<int:due_id>/', views.UpdateDue, name='update_due'),
		path('due/delete/<int:due_id>/', views.DeleteDue, name='delete_due'),

]