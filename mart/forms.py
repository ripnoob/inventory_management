from django import forms
from .models import Product, Purchase, Return

class AddProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['title', 'category', 'brand', 'price', 'quantity', 'is_refill']



class AddPurchaseForm(forms.ModelForm):
	class Meta:
		model = Purchase
		fields = ['product', 'supplier', 'quantity', 'cost', 'extra_cost', 'is_refill']


class AddReturnVoucher(forms.ModelForm):
	class Meta:
		model = Return
		fields = ['purchase', 'quantity', 'return_cost', 'issue']
				