from django.shortcuts import render, redirect, get_object_or_404
from .models import Sale, Due
from mart.models import Product
from accounts.models import Customer
from .forms import SaleForm, DueForm, DueStatusForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from django.views.decorators.cache import cache_page

# Create your views here.
login_required(login_url='accounts:login') 
def AddSale(request):
	products = Product.objects.all()
	customers = Customer.objects.all()

	if request.method == 'POST':
		form = SaleForm(request.POST)
		if form.is_valid():
			sale = form.save()
			messages.success(request, 'Sale record added.')

			paid = form.cleaned_data['paid']
			price = form.cleaned_data['prod_price']
			extra_cost = form.cleaned_data['extra_cost']
			quantity = form.cleaned_data['quantity']
			
			total = (price * quantity) + extra_cost

			if paid < total:
				due = Due.objects.create(
					sale = sale,
					due_amount = total - paid,
					is_paid = False 
					)
				messages.success(request, 'A sale and due record has been added.')


			return redirect('gross:view_sale')
		else:
			for field, errors in form.errors.items():
				for error in errors:
					messages.error(request, error)
					
	context = {'products':products, 'customers':customers}
	return render(request, 'gross/add_sale.html', context)

@cache_page(60*15)
@login_required(login_url='accounts:login')
def ViewSale(request):
	sale_record = Sale.objects.all()
	context = {'sale_record':sale_record}
	return render(request, 'gross/view_sale.html', context) 

def UpdateSale(request, sale_id):
	pass

login_required(login_url='accounts:login')
allowed_users(allowed_roles=['admin'])
def DeleteSale(request, sale_id):
	sale = get_object_or_404(Sale, pk=sale_id)
	if request.method == 'POST':
		sale.delete()
		messages.warning(request, 'Sale record has been deleted.')
	return redirect('gross:view_sale')


@cache_page(60*15)
@login_required(login_url='accounts:login')
def ViewDue(request):

	due = Due.objects.all()
	context = {'due_records':due}
	return render(request, 'gross/view_due.html', context)



login_required(login_url='accounts:login')
def AddDue(request):

	sale = Sale.objects.all()
	if request.method == 'POST':
		form = DueForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Due record has been added.')
			return redirect('gross:view_due')
		else:
			for field, errors in form.errors.items():
				for error in errors:
					messages.error(request, error)
	context = {'sales':sale}
	return render(request, 'gross/add_due.html', context)



login_required(login_url='accounts:login')
def UpdateDue(request, due_id):
    due = get_object_or_404(Due, id=due_id)

    if request.method == 'POST':
        form = DueStatusForm(request.POST, instance=due)
        if form.is_valid():
            is_paid = form.cleaned_data['is_paid']

            due.is_paid = is_paid
            due.save()

            if is_paid:
                sale = due.sale
                sale.paid += due.due_amount 
                sale.save()
                messages.success(request, 'Marked as paid and Sale updated.')
    else:
        form = DueStatusForm(instance=due)

    return redirect('gross:view_due')



@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def DeleteDue(request, due_id):
	due = get_object_or_404(Due, pk=due_id)
	if request.method == 'POST':
		due.delete()
		messages.warning(request, 'Due record deleted.')
	return redirect('gross:view_due')
	