from django.db import models
from blog.models import Post
from django.core.urlresolvers import reverse
#Note: only one object should be registered for the DTC class. The Events class is fine.
class DTC(models.Model):
	title = models.CharField(max_length = 50)
	description = models.TextField() 
	image = models.ImageField(upload_to='dtc_event')
class List(models.Model):
	name = models.CharField(max_length = 100)
	url = models.CharField(max_length=1000) #based on experience, FB event links tend to be long, so use tinyurl to shorten the length
	posts = models.ManyToManyField(Post, blank=True, related_name = "posts")
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('events:event_detail', kwargs = {'list_id':self.id})	
#Create your models here.
