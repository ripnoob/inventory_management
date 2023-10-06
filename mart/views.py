from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from accounts.decorators import allowed_users
from Inventory.models import Brand, Category
from .forms import AddProductForm
from django.contrib import messages
# Create your views here.

def product_view(request):
	product = Product.objects.all().order_by('-created_at')
	context = {'products':product}
	return render(request, 'mart/product.html', context)

def add_product(request):
	brand = Brand.objects.all()
	category = Category.objects.all()
	if request.method == 'POST':
		form = AddProductForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('mart:product')
		else:
			for field, errors in form.errors.items():
		 		for error in errors:
		 			messages.error(request, error)
	context = {'brand':brand, 'category':category}
	return render(request, 'mart/update_product.html', context)


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


def delete_product(request, product_id):
	pass