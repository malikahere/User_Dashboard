# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    password= forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = [
            'first_name', 'last_name', 'username', 'email', 'profile_picture', 'user_type',
            'address_line1', 'city', 'state', 'pincode', 'password', 'confirm_password'
        ]

    def clean_confirm_password(self):
        password= self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password and confirm_password and password!= confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return confirm_password
