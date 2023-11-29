from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import messages
from .models import Brand, Category, Supplier
from .forms import BrandForm, CategoryForm, SupplierForm
from django.http import JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users

# Create your views here.
@login_required(login_url='accounts:login')
def DashBoard(request):
	return render(request, 'inventory/dashboard.html')

@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def AddBrand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Brand added successfully.')
            return redirect('inventory:all_brand') 
    else:
        form = BrandForm()
    return render(request, 'inventory/add_brand.html', {'form': form})

@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def UpdateBrand(request, brand_id):

    brand = get_object_or_404(Brand, pk=brand_id)

    if request.method == 'POST':
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            messages.success(request, 'Brand updated successfully.')
            return redirect('inventory:all_brand')
    else:
        form = BrandForm(instance=brand)

    return render(request, 'inventory/update_brand.html', {'form': form, 'brand': brand})




@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def DeleteBrand(request, brand_id):

    brand = get_object_or_404(Brand, pk=brand_id)

    if request.method == 'POST':
        brand.delete()
        messages.warning(request, 'Brand removed successfully.')

    return redirect('inventory:all_brand')

	
@login_required(login_url='accounts:login')
def AllBrand(request):
	all_brand = Brand.objects.all().order_by('-created_at')
	context = {
		'brands':all_brand,
	}
	return render(request, 'inventory/all_brand.html', context)


@login_required(login_url='accounts:login')
def ViewCategory(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request, 'inventory/category/view_category.html', context)


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def AddCategory(request):

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully.')
            return redirect('inventory:view_category')
    else:
        form = CategoryForm()

    return render(request, 'inventory/category/add_category.html')



@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def DeleteCategory(request, category_id):

    category = get_object_or_404(Category, pk=category_id)

    if request.method == 'POST':
        category.delete()
        messages.warning(request, 'Category removed successfully.')
    return redirect('inventory:view_category')



@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def UpdateCategory(request, category_id):
    category = get_object_or_404(Category, pk=category_id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully.')
            return redirect('inventory:view_category')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'inventory/category/add_category.html', {'form': form, 'category': category})





def ViewSupplier(request):
    suppliers = Supplier.objects.all()
    context = {'suppliers':suppliers}
    return render(request, 'inventory/view_supplier.html', context)



@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def AddSupplier(request):
    brand = Brand.objects.all()
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Supplier added successfully.')
            return redirect('inventory:view_supplier')
    return render(request, 'inventory/add_supplier.html', {'brand':brand})
    
@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def DeleteSupplier(request, supplier_id):
    supplier = get_object_or_404(Supplier, pk=supplier_id)
    if request.method == 'POST':
        supplier.delete()
        messages.warning(request, 'Supplier has been removed.')
    return redirect('inventory:view_supplier')    

def UpdateSupplier(request):
    pass