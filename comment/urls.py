from django.urls import path
from . import views

urlpatterns = [
    path('comment/<int:doctor_id>/<int:visit_id>/', views.create_comment, name='create_comment'),
    path('doctor/<int:doctor_id>/comments/', views.doctor_comments, name='doctor_comments'),
]
