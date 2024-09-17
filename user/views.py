from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, LoginForm, UpdateUserForm, UpdateProfileForm, UpdateDoctorForm


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # Load the profile instance created by the signal
            user.profile.full_name = form.cleaned_data.get('full_name')
            user.profile.phone_number = form.cleaned_data.get('phone_number')
            user.profile.wallet_id = form.cleaned_data.get('wallet_id')
            user.profile.is_admin = form.cleaned_data.get('is_admin')
            user.profile.email = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request, 'ثبت‌نام با موفقیت انجام شد!')
            return redirect('home')
        else:
            messages.error(request, 'لطفاً فرم را به درستی پر کنید.')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'ورود با موفقیت انجام شد!')
                # TODO: Redirect to user profile page
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
        profile_form = UpdateProfileForm(
            request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'پروفایل شما با موفقیت به‌روزرسانی شد.')
            return redirect('profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def edit_doctor(request):
    if request.method == 'POST':
        doctor_form = UpdateDoctorForm(
            request.POST, instance=request.user.doctor)
        if doctor_form.is_valid():
            doctor_form.save()
            messages.success(
                request, 'پروفایل پزشکی شما با موفقیت به‌روزرسانی شد.')
            return redirect('profile')
    else:
        doctor_form = UpdateDoctorForm(instance=request.user.doctor)
    return render(request, 'edit_doctor.html', {'doctor_form': doctor_form})
