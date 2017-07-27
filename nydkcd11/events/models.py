from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from django.db import models
from blog.models import Post
from django.urls import reverse
#Note: only one object should be registered for the DTC class. The Events class is fine.
class Convention(models.Model):
	title = models.CharField(max_length = 75)
	background_image = models.ImageField(upload_to = "conventions")
	def_short = RichTextField()
	video = EmbedVideoField()
	def __str__(self):
		return self.title
class Part(models.Model):
	header = models.CharField(max_length = 75)
	body = RichTextField()
	image = models.ImageField(upload_to="conventions")
	convention = models.ForeignKey(Convention, on_delete = models.CASCADE)
	def __str__(self):
		return self.header
class DTC(models.Model):
	title = models.CharField(max_length = 50)
	description = models.TextField() 
	image = models.ImageField(upload_to='dtc_event')
class List(models.Model):
	name = models.CharField(max_length = 100)
	url = models.CharField(max_length=1000) #based on experience, FB event links tend to be long, so use tinyurl to shorten the length
	posts = models.ManyToManyField(Post, blank=True, related_name = "posts")
	slug = models.SlugField()
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('events:event_detail', kwargs = {'list_id':self.id, 'slug':self.slug})	
	def save(self):
		self.slug = slugify(self.name)
		super(List, self).save()

#Create your models here.
