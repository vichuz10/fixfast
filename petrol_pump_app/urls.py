from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.petrol_pump_register, name='petrol_pump_register'),
    path('dashboard/', views.petrol_pump_dashboard, name='petrol_pump_dashboard'),
]
