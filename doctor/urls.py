from django.urls import path
from . import views

app_name = 'doctor'
urlpatterns = [
    path('book/<int:doctor_id>/', views.book_visit, name='book_visit'),
    path('<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
]