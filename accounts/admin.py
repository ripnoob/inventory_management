from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Customer
from .forms import StaffForm, CreateUserForm


class AdminCustomUser(UserAdmin):
	model = CustomUser
	add_form = StaffForm

	fieldsets = (
		*UserAdmin.fieldsets,
								('Access', {'fields': ('role',)}
								),
								('Other', {'fields': ('phone_number',)}
								),

		)



admin.site.register(CustomUser, AdminCustomUser)


class AdminCustomerView(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'last_name', 'phone', 'address']

admin.site.register(Customer, AdminCustomerView)