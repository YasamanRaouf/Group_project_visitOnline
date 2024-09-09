from django.shortcuts import render
from .models import Doctor

def doctor_detail_view(request, doctor_id): 
    doctor = Doctor.objects.get(doctor_id=doctor_id)
    return render(request, 'doctor/doctor_detail.html', {'doctor': doctor})
