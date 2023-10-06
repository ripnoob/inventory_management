from django import forms
from .models import Brand, Category

class BrandForm(forms.ModelForm):
    
    class Meta:
        model = Brand
        fields = ['name', 'email', 'phone', 'address']

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['weight']