from django.urls import path
from . import views

app_name = 'doctor'
urlpatterns = [
    path('', views.DoctorListView, name='Doctor_list'),
    path('', views.DoctorSearchView, name='Doctor_Search'),
]