from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    number = models.CharField(max_length=15, null=True, blank=True)
