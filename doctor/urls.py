from django.urls import path
from . import views

urlpatterns = [
    path('', views.DoctorListView, name='Doctor_list'),
    path('', views.DoctorSearchView, name='Doctor_Search'),
]