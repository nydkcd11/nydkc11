from django.db import models
class Newsletter(models.Model):
	month = models.CharField(max_length = 30)
	url = models.CharField(max_length=100)
	def __str__(self):
		return str(self.month)
class Minutes(models.Model):
	month = models.DateField()
	url = models.CharField(max_length=100)
	def __str__(self):
		return str(self.month)
# Create your models here.
