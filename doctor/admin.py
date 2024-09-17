from django.contrib import admin
from .models import Doctor
from user.models import Profile

@admin.register(Doctor,Profile)
class DoctorAdmin(admin.ModelAdmin):
    list_display = [
        'doctor_id',
        'user__full_name',
        'specialty',
        'price',
        'is_active',
    ]
    
    sortable_by = [
        'doctor_id',
    ]
    
    list_editable = [
        'user__full_name',
        'specialty',
        'price',
        'is_active',  
    ]
    
    search_fields = [
        'doctor_id',
        'user__full_name',
    ]

# Register your models here.
