from django.db import models
class Division(models.Model):
	name = models.CharField(max_length = 100)
	school = models.CharField(max_length = 75)
	position = models.CharField(max_length = 50)
	desc = models.TextField()
	image = models.ImageField(upload_to='division_photos/')
	def __str__(self):
		return self.name
class School(models.Model):
	school = models.CharField(max_length = 100)
	pres = models.CharField(max_length = 75, default = "N/A")
	vicepres = models.CharField(max_length = 75, default = "N/A")
	secretary = models.CharField(max_length = 75, default = "N/A")
	treasurer = models.CharField(max_length = 75, default = "N/A")
	webmaster = models.CharField(max_length = 75, default = "N/A")
	editor = models.CharField(max_length = 75, default = "N/A")
	url = models.CharField(max_length = 300, default = "#")
	image = models.ImageField(upload_to='school_photos/')
	def __str__(self):
		return self.school	
class FAQ(models.Model):
	question = models.CharField(max_length = 300)
	answer = models.TextField()
	def __str__(self):
		return self.question
# Create your models here.
