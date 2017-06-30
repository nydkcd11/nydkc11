from django.db import models

class Contact(models.Model):
	name=models.CharField(max_length=50)
	school = models.CharField(max_length=50)
	email=models.CharField(max_length=50)
	title=models.CharField(max_length=50)
	message = models.TextField()
	def __str__(self):
		return self.title
class Email(models.Model):
	email = models.CharField('Email: ',max_length = 50)
	def __str__(self):
		return self.email
# Create your models here.
