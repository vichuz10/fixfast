from django.contrib.auth.models import User
from django.db import models

class PetrolPump(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
