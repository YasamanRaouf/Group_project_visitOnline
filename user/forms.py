from django import forms
from django.contrib.auth.models import User
from doctor.models import Doctor
from django import forms
from .models import User


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'full_name', 'phone_number', 'wallet_id',
                  'is_admin', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }


class LoginForm(forms.Form):
    email = forms.CharField(
        max_length=100, required=True, help_text='Email')
    password = forms.CharField(
        max_length=100, required=True, help_text='Password', widget=forms.PasswordInput())


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'full_name',
                  'phone_number', 'wallet_id', 'is_admin']


class AddDoctorForm(forms.ModelForm):
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
        fields = ['specialty', 'price', 'user']

    def save(self, commit=True):
        doctor = super(AddDoctorForm, self).save(commit=False)
        doctor.availability = Doctor.availability_dict(
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


class UpdateDoctorForm(forms.ModelForm):
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
        doctor = super(UpdateDoctorForm, self).save(commit=False)
        doctor.availability = Doctor.availability_dict(
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
