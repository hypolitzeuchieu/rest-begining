from django.db import models
from accounts.models import UserAccount


class Product(models.Model):
    user = models.ForeignKey(UserAccount, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    due_date = models.DateTimeField()
    image = models.ImageField(upload_to='picture')

    def __str__(self):
        return self.name
