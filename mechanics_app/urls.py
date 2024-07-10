from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.mechanic_register, name='mechanic_register'),
    path('dashboard/', views.mechanic_dashboard, name='mechanic_dashboard'),
]
