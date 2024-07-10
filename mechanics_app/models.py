from django.contrib.auth.models import User
from django.db import models

class Mechanic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_location = models.CharField(max_length=255)
    services_provided = models.TextField()
