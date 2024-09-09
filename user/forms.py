from django import forms

from .models import User


class UserSignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'phone_number', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
