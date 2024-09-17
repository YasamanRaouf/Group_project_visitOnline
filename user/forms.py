from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from doctor.models import Doctor


class SignUpForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=100, required=True, help_text='Full Name')
    phone_number = forms.CharField(
        max_length=15, required=True, help_text='Phone Number')
    wallet_id = forms.CharField(
        max_length=50, required=True, help_text='Wallet ID')
    is_admin = forms.BooleanField(required=False, help_text='Is Admin')
    email = forms.EmailField(
        max_length=200, required=True, help_text='Email Address')

    class Meta:
        model = User
        fields = ('username', 'full_name', 'phone_number', 'wallet_id',
                  'is_admin', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100, required=True, help_text='Username')
    password = forms.CharField(
        max_length=100, required=True, help_text='Password', widget=forms.PasswordInput())


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'phone_number', 'wallet_id', 'is_admin']


class UpdateDoctorFrom(forms.ModelForm):
    saturday = forms.CharField(max_length=100, required=False)
    sunday = forms.CharField(max_length=100, required=False)
    monday = forms.CharField(max_length=100, required=False)
    tuesday = forms.CharField(max_length=100, required=False)
    wednesday = forms.CharField(max_length=100, required=False)
    thursday = forms.CharField(max_length=100, required=False)
    friday = forms.CharField(max_length=100, required=False)
    interval = forms.IntegerField(required=True)

    class Meta:
        model = Doctor
        fields = ['specialty', 'price']

    def save(self, commit=True):
        doctor = super(UpdateDoctorFrom, self).save(commit=False)
        doctor.availability = Doctor.default_availability(
            saturday=self.cleaned_data['saturday'],
            sunday=self.cleaned_data['sunday'],
            monday=self.cleaned_data['monday'],
            tuesday=self.cleaned_data['tuesday'],
            wednesday=self.cleaned_data['wednesday'],
            thursday=self.cleaned_data['thursday'],
            friday=self.cleaned_data['friday'],
            interval=self.cleaned_data['interval'],
        )
        if commit:
            doctor.save()
        return doctor
