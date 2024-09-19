from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, LoginForm, UpdateUserForm, UpdateDoctorForm, AddDoctorForm

from .models import User, Wallet


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:login')
        else:
            messages.error(request, 'لطفاً فرم را به درستی پر کنید.')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.get(email=email)
            if user is not None:
                if user.password == password:
                    messages.success(request, 'ورود با موفقیت انجام شد!')
                    print("Hooraay")
                return redirect('home')
            else:
                messages.error(request, 'نام کاربری یا رمز عبور اشتباه است.')
        else:
            messages.error(request, 'لطفاً فرم را به درستی پر کنید.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'پروفایل شما با موفقیت به‌روزرسانی شد.')
            return redirect('profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
    return render(request, 'edit_profile.html', {'user_form': user_form})


def edit_doctor(request, doctor_id):
    doctor = User.objects.get(id=doctor_id)
    if request.method == 'POST':
        doctor_form = UpdateDoctorForm(request.POST, instance=doctor)
        if doctor_form.is_valid():
            doctor_form.save()
            messages.success(request, 'پروفایل پزشک با موفقیت به‌روزرسانی شد.')
            return redirect('profile')
    else:
        doctor_form = UpdateDoctorForm(instance=doctor)


def add_doctor(request):
    if request.method == 'POST':
        form = AddDoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:login')
        else:
            messages.error(request, 'لطفاً فرم را به درستی پر کنید.')
    else:
        form = AddDoctorForm()
    return render(request, 'add_doctor.html', {'form': form})
