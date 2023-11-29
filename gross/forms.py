from django import forms
from .models import Sale, Due

class SaleForm(forms.ModelForm):
	
	class Meta:
		model = Sale
		fields = ['product', 'customer', 'prod_price', 'extra_cost', 'paid', 'quantity', 'is_refill', 'is_wholesale']

		extra_cost = forms.FloatField(initial=0.0)


class DueForm(forms.ModelForm):

	class Meta:
		model = Due
		fields = ['sale', 'due_amount', 'is_paid']


class DueStatusForm(forms.ModelForm):

	class Meta:
		model = Due
		fields = ['is_paid']
		widgets = {
		'is_paid': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
