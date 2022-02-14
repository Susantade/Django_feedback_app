
from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=50, blank=False)
    password = models.CharField(max_length=50)
    secret = models.CharField(max_length=50)
    comment = models.TextField(default='', max_length=5000)