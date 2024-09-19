from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, LoginForm, UpdateUserForm, UpdateDoctorForm



def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'ثبت‌نام با موفقیت انجام شد!')
                return redirect('home')
            else:
                messages.error(request, 'خطا در ورود. لطفاً دوباره تلاش کنید.')
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
            user = authenticate(email=email, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'ورود با موفقیت انجام شد!')
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

@login_required
def edit_doctor(request):
    if hasattr(request.user, 'doctor'):
        if request.method == 'POST':
            doctor_form = UpdateDoctorForm(request.POST, instance=request.user.doctor)
            if doctor_form.is_valid():
                doctor_form.save()
                messages.success(request, 'پروفایل پزشکی شما با موفقیت به‌روزرسانی شد.')
                return redirect('profile')
        else:
            doctor_form = UpdateDoctorForm(instance=request.user.doctor)
        return render(request, 'edit_doctor.html', {'doctor_form': doctor_form})
    else:
        messages.error(request, 'شما پزشک نیستید یا پروفایل پزشک شما وجود ندارد.')
        return redirect('home')