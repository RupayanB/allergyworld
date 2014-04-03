from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)
