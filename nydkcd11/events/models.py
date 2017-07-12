from django.db import models
from blog.models import Post
#Note: only one object should be registered for the DTC class. The Events class is fine.
class DTC(models.Model):
	title = models.CharField(max_length = 50)
	description = models.TextField() 
	image = models.ImageField(upload_to='dtc_event')
class List(models.Model):
	name = models.CharField(max_length = 100)
	url = models.CharField(max_length=1000) #based on experience, FB event links tend to be long, so use tinyurl to shorten the length
	posts = models.ManyToManyField(Post, blank=True, related_name = "posts")
#Create your models here.
