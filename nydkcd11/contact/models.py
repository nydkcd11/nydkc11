from django.db import models

class Contact(models.Model):
	name=models.CharField(max_length=50)
	school = models.CharField(max_length=50)
	email=models.CharField(max_length=50)
	title=models.CharField(max_length=50)
	text=models.TextField()
	def __str__(self):
		return self.title
# Create your models here.
