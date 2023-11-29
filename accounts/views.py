from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, StaffForm, AdminForm, CustomerForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from .decorators import allowed_users
from .models import CustomUser, Customer
from django.contrib.auth.decorators import login_required
# Create your views here.

@allowed_users(allowed_roles=['admin'])
def register_view(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.role = request.POST['role']
			form.save()
			messages.success(request, 'User successfully created.')
			return redirect('inventory:dashboard')
		else:
		 	for field, errors in form.errors.items():
		 		for error in errors:
		 			messages.error(request, error)

	context = {'form':form}
	return render(request, 'accounts/register.html', context)



def login_view(request):
	if request.user.is_authenticated:
		return redirect('inventory:dashboard')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				messages.success(request, 'User successfully logged in.')
				return redirect('inventory:dashboard')
			else:
				messages.error(request, 'username or password is incorrect.')
				return redirect('accounts:login')

	return render(request, 'accounts/login.html')


def logout_view(request):
	if request.user.is_authenticated:
		logout(request)
		messages.success(request, 'user successfully logged out.')
		return redirect('accounts:login')


# Staff Views		

@login_required(login_url='accounts:login')
def staff_view(request):
	staff = CustomUser.objects.filter(role='staff')
	context = {'staffs':staff}
	return render(request, 'accounts/manage_staff.html', context)

@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def delete_staff(request, staff_id):
	staff = get_object_or_404(CustomUser, pk=staff_id)
	if request.method == 'POST':
		staff.delete()
		messages.success(request, 'Staff account withdraded successfully.')
	return redirect('accounts:staff')


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def update_staff(request, staff_id):
	form = StaffForm()
	staff = CustomUser.objects.get(id=staff_id)
	if request.method == 'POST':
		form = StaffForm(request.POST, instance=staff)
		if form.is_valid():
			form.save()
			messages.success(request, 'Information updated.')
			return redirect('accounts:staff')
		else:
			for field, errors in form.errors.items():
		 		for error in errors:
		 			messages.error(request, error)

	return render(request, 'accounts/update_staff.html', {'form':form, 'staff':staff})



# Admin Views

@login_required(login_url='accounts:login')
def AdminView(request):
	admin = CustomUser.objects.filter(role='admin')
	context = {'admins':admin}
	return render(request, 'accounts/manage_admin.html', context)


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def update_admin(request, admin_id):
	form = AdminForm()
	admin = CustomUser.objects.get(id=admin_id)
	if request.method == 'POST':
		form = AdminForm(request.POST, instance=admin)
		if form.is_valid():
			form.save()
			messages.success(request, 'Information updated.')
			return redirect('accounts:admin')
		else:
			form = AdminForm(instance=admin)

	return render(request, 'accounts/update_admin.html', {'form':form, 'admin':admin})

@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def delete_admin(request, admin_id):
	admin = get_object_or_404(CustomUser, pk=admin_id)
	if request.method == 'POST':
		admin.delete()
		messages.success(request, 'Admin account withdraded successfully.')
	return redirect('accounts:admin')



# Customer Views

def CustomerView(request):
	customers = Customer.objects.all().order_by('-created_at')
	context = {'customers':customers}
	return render(request, 'accounts/customer/customer_list.html', context)

@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin','staff'])
def add_customer(request):
	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Customer has been added successfully.')
			return redirect('accounts:customer')
		else:
			form.CustomerForm()
			for field, errors in form.errors.items():
		 		for error in errors:
		 			messages.error(request, error)

	return render(request, 'accounts/customer/add_customer.html')



def update_customer(request, customer_id):
	customer = get_object_or_404(Customer, pk=customer_id)
	if request.method == 'POST':
		form = CustomerForm(request.POST, instance=customer)
		if form.is_valid():
			form.save()
			messages.success(request, 'Information updated successfully.')
			return redirect('accounts:customer')
		else:
			form.CustomerForm()
			for field, errors in form.errors.items():
		 		for error in errors:
		 			messages.error(request, error)
	context = {'customer':customer}
	return render(request, 'accounts/customer/add_customer.html', context)


def delete_customer(request, customer_id):
	customer = get_object_or_404(Customer, pk=customer_id)
	if request.method == 'POST':
		customer.delete()
		messages.success(request, f'Customer ({customer.first_name}) has been removed successfully.')
	return redirect('accounts:customer')