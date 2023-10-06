from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [

	path('account/register/', views.register_view, name='register'),
	path('', views.login_view, name='login'),
	path('account/logout/', views.logout_view, name='logout'),

	path('account/staff', views.staff_view, name='staff'),
	path('account/reject-staff/<int:staff_id>/', views.delete_staff, name='delete_staff'),
	path('account/update-staff/<int:staff_id>/', views.update_staff, name='update_staff'),

	path('account/admin/', views.AdminView, name='admin'),
	path('account/reject-admin/<int:admin_id>/', views.delete_admin, name='delete_admin'),
	path('account/update-admin/<int:admin_id>/', views.update_admin, name='update_admin'),

	path('account/customer/', views.CustomerView, name='customer'),
	path('account/add-customer/', views.add_customer, name='add_customer'),
	path('account/update-info/<int:customer_id>/', views.update_customer, name='update_customer'),
	path('account/remove-customer/<int:customer_id>/', views.delete_customer, name='delete_customer'),
]