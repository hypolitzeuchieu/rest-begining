from django.db import models
from django.contrib.auth.models import User


class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.username
