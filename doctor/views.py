from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from models import Doctor
from django.db.models import Q 


class DoctorListView(LoginRequiredMixin,ListView):
    model = Doctor
    template_name = 'doctor/doctor_Form.html'
    
    def get_queryset(self):
        return Doctor.objects.filter(
            is_active = True).values(
                'user__full_name', 'specialty__spec_name'
            )
    
    
class DoctorSearchView(LoginRequiredMixin,ListView):
    model = Doctor
    template_name = 'doctor/doctor_Search.html'
    
    def get_queryset(self):
        search_item = self.request.GET.get('search_item', '')
        if search_item:
            return Doctor.objects.filter(
                Q(specialty__icontains=search_item) | 
                Q(user__full_name__icontains=search_item )
            ).filter(is_active=True).values(
                'user__full_name', 'specialty__spec_name' ,'availability'
            )
       
# Create your views here.