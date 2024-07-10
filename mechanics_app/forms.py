from django import forms
from django.contrib.auth.models import User
from .models import Mechanic

class MechanicRegistrationForm(forms.ModelForm):
    class Meta:
        model = Mechanic
        fields = ['shop_location', 'services_provided']
