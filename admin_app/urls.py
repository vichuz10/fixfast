from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.admin_register, name='admin_register'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
