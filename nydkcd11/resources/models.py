from django.db import models
class Newsletter(models.Model):
	month = models.DateField()
	url = models.CharField(max_length=100)
class Minutes(models.Model):
	month = models.DateField()
	url = models.CharField(max_length=100)
# Create your models here.
