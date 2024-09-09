from django.urls import path
from . import views

urlpatterns = [
    path('', views.wallet_list, name='wallet_list'),
    path('<int:wallet_id>/', views.wallet_detail, name='wallet_detail'),
    path('create/', views.create_wallet, name='create_wallet'),
]