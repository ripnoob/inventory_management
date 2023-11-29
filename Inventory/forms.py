from django import forms
from .models import Brand, Category, Supplier

class BrandForm(forms.ModelForm):
    
    class Meta:
        model = Brand
        fields = ['name', 'email', 'phone', 'address']

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['weight']



class SupplierForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = ['brand', 'contact_name', 'address', 'phone']