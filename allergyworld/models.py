from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)
    rating = models.CharField(max_length=10)
    price_level = models.CharField(max_length=10)

class UserManager(models.Manager):
	def create_user(self, name, allergy, email):
		user = self.create(name=name,allergy=allergy,email=email)
		return user

class User(models.Model):
	name = models.CharField(max_length=100)
	allergy = models.CharField(max_length=100)
	email = models.CharField(max_length=100)

	objects = UserManager()
