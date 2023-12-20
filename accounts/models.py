from django.db import models
from django.contrib.auth.models import AbstractUser


class UserAccount(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
