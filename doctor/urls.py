from django.urls import path
from .views import DoctorListView, DoctorSearchView, book_visit, doctor_detail, visited_doctors_list

app_name = 'doctor'
urlpatterns = [
    path('book/<int:doctor_id>/', book_visit, name='book_visit'),
    path('<int:doctor_id>/', doctor_detail, name='doctor_detail'),
    path('visited/', visited_doctors_list, name='visited_doctors_list'),
    path('list/', DoctorListView.as_view(), name='doctor_list'),
    path('search/', DoctorSearchView.as_view(), name='doctor_search'),
]
