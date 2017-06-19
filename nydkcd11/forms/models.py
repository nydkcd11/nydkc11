from django.db import models
class Papers(models.Model):
	name = models.CharField(max_length = 30)
	url = models.CharField(max_length = 300) 
	def __str__(self):
		return self.name
# Create your models here.
