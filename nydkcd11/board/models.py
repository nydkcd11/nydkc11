from django.db import models

# Create your models here.

class Person(models.Model):
	name = models.CharField(max_length = 50)
	school = models.CharField(max_length = 75)
	position = models.CharField(max_length = 50)
	desc = models.CharField(max_length = 300)
	image = models.ImageField()
	#addd sub functions from shell

