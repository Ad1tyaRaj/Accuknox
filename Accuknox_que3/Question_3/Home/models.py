from django.db import models

# Create your models here.

class MyModel(models.Model):
    objects = None
    name = models.CharField(max_length=100)