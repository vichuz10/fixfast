from django import forms
from django.contrib.auth.models import User
from .models import PetrolPump

class PetrolPumpRegistrationForm(forms.ModelForm):
    class Meta:
        model = PetrolPump
        fields = ['location']
