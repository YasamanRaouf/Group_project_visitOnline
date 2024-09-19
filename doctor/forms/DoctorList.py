from django import forms
from visitonline.doctor.models import Doctor

class DoctorListForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['user__full_name' , 'specialty__spec_name']