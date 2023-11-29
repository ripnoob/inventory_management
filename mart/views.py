from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Purchase, Return
from accounts.decorators import allowed_users
from Inventory.models import Brand, Category, Supplier
from .forms import AddProductForm, AddPurchaseForm, AddReturnVoucher
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
# Create your views here.

def product_view(request):
	product = Product.objects.all().order_by('-created_at')
	context = {'products':product}
	return render(request, 'mart/product.html', context)

	
@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def add_product(request):

    brand = Brand.objects.all()
    category = Category.objects.all()

    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            # Check for duplicate entries before saving
            if not Product.objects.filter(title=form.cleaned_data['title']).exists():
                form.save()
                return redirect('mart:product')
            else:
                messages.error(request, 'Product with this title already exists.')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)

    context = {'brand': brand, 'category': category}
    return render(request, 'mart/update_product.html', context)


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def update_product(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	brand = Brand.objects.all()
	category = Category.objects.all()
	prod_cat = get_object_or_404(Category, pk=product.category.id)
	prod_brand = get_object_or_404(Brand, pk=product.brand.id)

	if request.method == 'POST':
		form = AddProductForm(request.POST, instance=product)
		if form.is_valid():
			form.save()
			messages.success(request, 'Product updated successfully.')
			return redirect('mart:product')
		else:
			for field, errors in form.errors.items():
				for error in errors:
					messages.error(request, error)
	context = {'brand':brand, 'category':category, 'product':product, 'prod_cat': prod_cat, 'prod_brand':prod_brand }
	return render(request, 'mart/update_product.html', context)

@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def delete_product(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	if request.method == 'POST':
		product.delete()

	messages.warning(request, f'{product.title} has been removed.')
	return redirect('mart:product')


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def add_purchase(request):
	
	product = Product.objects.all()
	supplier = Supplier.objects.all()
	
	if request.method == 'POST':
		form = AddPurchaseForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Purchase record successfully added.')
			return redirect('mart:view_purchase')
		else:
			for field, errors in form.errors.items():
				for error in errors:
					messages.error(request, error)

	context = {'product':product, 'supplier':supplier}
	return render(request, 'mart/purchase.html', context)

	

@login_required(login_url='accounts:login')	
def view_purchase(request):
	purchases = Purchase.objects.all()
	context = {'purchases':purchases}
	return render(request, 'mart/purchase_record.html', context)

@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def delete_purchase(request, purchase_id):
	purchase = get_object_or_404(Purchase, pk=purchase_id)
	if request.method == 'POST':
		purchase.delete()
		messages.warning(request, 'Purchase record has been removed successfully.')
	return redirect('mart:view_purchase')

def update_purchase(request):
	pass


@login_required(login_url='accounts:login')
def view_return(request):
	return_voucher = Return.objects.all()
	context = {'return_voucher':return_voucher }
	return render(request, 'mart/views_return.html', context)



@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def add_return(request):
	purchase = Purchase.objects.all()
	if request.method == 'POST':
		form = AddReturnVoucher(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Return voucher added.')
			return redirect('mart:view_return')
		else:
			for field, errors in form.errors.items():
				for error in errors:
					messages.error(request, 'error')
	context = {'purchase': purchase}
	return render(request, 'mart/return.html', context)



@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def update_return(request, return_id):
	pass



@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def delete_return(request, return_id):
	return_record = get_object_or_404(Return, pk=return_id)
	if request.method == 'POST':
		return_record.delete()
		messages.warning(request, 'A return record has been removed.')
	return redirect('mart:view_return')