from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomUser(User):
    country = models.CharField(null=True, blank=True, max_length=100)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    nickname = models.CharField(max_length=40, blank=True)
    image = models.ImageField(blank=True)
