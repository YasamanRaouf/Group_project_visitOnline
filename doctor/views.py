from datetime import datetime
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Doctor, Visit
from django.utils import timezone
from django.shortcuts import render


class DoctorListView(LoginRequiredMixin, ListView):
    model = Doctor
    template_name = 'forms/doctorList.html'

    def get_queryset(self):
        return Doctor.objects.filter(
            is_active=True).values(
                'user__full_name', 'specialty__spec_name'
        )


class DoctorSearchView(LoginRequiredMixin, ListView):
    model = Doctor
    template_name = 'forms/doctorSearch.html'

    def get_queryset(self):
        search_item = self.request.GET.get('search_item', '')
        if search_item:
            return Doctor.objects.filter(
                Q(specialty__icontains=search_item) |
                Q(user__full_name__icontains=search_item)
            ).filter(is_active=True).values(
                'user__full_name', 'specialty__spec_name', 'availability'
            )


class DateInput(forms.DateInput):
    input_type = "date"


class TimeInput(forms.TimeInput):
    input_type = "time"
    format = '%H:%M'


class BookingForm(forms.Form):
    date = forms.DateField(widget=DateInput())
    time = forms.TimeField(widget=TimeInput())


def book_visit(request, doctor_id):
    doctor = get_object_or_404(Doctor, doctor_id=doctor_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            time = datetime.strptime(time.strftime('%H:%M'), '%H:%M').time()
            datetime_combined = timezone.make_aware(
                datetime.combine(date, time))
            available_slots = doctor.get_available_slots(
                date.strftime('%A').lower())
            for slot in available_slots:
                interval = slot.split('-')
                start_time = datetime.strptime(interval[0], '%H:%M').time()
                end_time = datetime.strptime(interval[1], '%H:%M').time()
                print(start_time, time, end_time)
                if start_time <= time <= end_time:
                    visit = Visit.objects.create(
                        doctor=doctor,
                        user=request.user,
                        date_time=datetime_combined
                    )
                    visit.save()
                    print(visit)

                return HttpResponse("Appointment booked successfully! Please proceed to payment.")
            else:
                return HttpResponse("Selected time is not available.", status=400)
    else:
        form = BookingForm()

    context = {
        'doctor': doctor,
        'form': form,
        'available_slots': doctor.get_available_slots(request.GET.get('date'))
    }
    return render(request, 'book_appointment.html', context)


def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor, doctor_id=doctor_id)
    context = {
        'doctor': doctor,
        'available_slots': doctor.get_available_slots(datetime.now().strftime('%A').lower())
    }
    return render(request, 'doctor_detail.html', context)


def visited_doctors_list(request):
    user = request.user
    visits = Visit.objects.filter(user=user).select_related('doctor')

    context = {
        'visits': visits,
    }
    return render(request, 'visited_doctors_list.html', context)
