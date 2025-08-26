from django.db import models # type: ignore
from django.contrib.auth.models import AbstractUser  # type: ignore
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.username
