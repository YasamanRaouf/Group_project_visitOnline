from django.urls import path
from .views import signup_view, edit_profile

app_name = 'user'

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('edit_profile/', edit_profile, name='edit_profile'),
]
