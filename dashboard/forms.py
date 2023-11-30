from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from accounts.models import CustomUser

class AccountUpdateForm(forms.ModelForm):
    current_password = forms.CharField(
        label='Current Password',
        widget=forms.PasswordInput,
        required=False,
    )

    new_password = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput,
        required=False,
    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number']

    def clean_new_password(self):
        new_password = self.cleaned_data.get('new_password')
        
        if new_password:
        	validate_password(new_password, self.instance)
        return new_password

    def clean(self):
        cleaned_data = super().clean()
        current_password = cleaned_data.get('current_password')
        user = self.instance

        if current_password and not authenticate(username=user.username, password=current_password):
            raise forms.ValidationError('Invalid current password.')

        return cleaned_data
