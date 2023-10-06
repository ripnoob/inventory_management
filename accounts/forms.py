from django import forms
from .models import CustomUser, Customer
from django.contrib.auth.forms import UserCreationForm



class CreateUserForm(UserCreationForm):

    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('staff', 'Staff'),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES)
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']


class StaffForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'role',]



class AdminForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'role',]



class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"