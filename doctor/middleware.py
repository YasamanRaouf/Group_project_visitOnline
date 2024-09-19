from django.shortcuts import redirect
from django.urls import reverse

class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        # Check if the user is logged in and trying to access admin panel
        if request.user.is_authenticated and request.path.startswith(reverse('admin:index')):
            if not request.user.is_admin:
                # Redirect to home or an error page if not an admin
                return redirect('home')  # Adjust to your redirect URL

        response = self.get_response(request)
        return response