from django.urls import path
from .views import create_comment, doctor_comments


app_name = 'comment'
urlpatterns = [
    path('<int:doctor_id>/<int:visit_id>/',
         create_comment, name='create_comment'),
    path('doctor/<int:doctor_id>/comments/',
         doctor_comments, name='doctor_comments'),
]
