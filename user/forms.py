from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True, help_text='Full Name')
    phone_number = forms.CharField(max_length=15, required=True, help_text='Phone Number')
    wallet_id = forms.CharField(max_length=50, required=True, help_text='Wallet ID')
    is_admin = forms.BooleanField(required=False, help_text='Is Admin')
    email = forms.EmailField(max_length=200, required=True, help_text='Email Address')

    class Meta:
        model = User
        fields = ('username', 'full_name', 'phone_number', 'wallet_id', 'is_admin', 'email', 'password1', 'password2')

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'phone_number', 'wallet_id', 'is_admin']
