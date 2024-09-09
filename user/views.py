from django.shortcuts import render
from .forms import UserSignupForm


def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})
