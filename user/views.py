from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import SignUpForm

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
