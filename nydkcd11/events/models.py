from dateutil.parser import parse
from blog.image_compress import compress
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from django.db import models
from blog.models import Post
from django.urls import reverse
from projects.colorgen import hexgen
from events.facebook_event_api.api_side import *
#This lists out the various conventions D11 holds (e.g. LTC)
class Convention(models.Model):
	title = models.CharField(max_length = 75,verbose_name="Name of Convention")
	background_image = models.ImageField(upload_to = "conventions")
	def_short = RichTextField(verbose_name="Short Explanation of Convention")
	video = EmbedVideoField()
	slug = models.SlugField(blank=True)
	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('events:long_event', kwargs = {'convention_id':self.id, 'slug':self.slug})
	def save(self):
		self.slug = slugify(self.title)
		self.background_image = compress(self.background_image)
		super(Convention, self).save()
#the unique part about conventions is that it has smaller "parts" explaining different aspects of the convention
#They are expressed in a different table and linked to their convetnions using foreign keys 
#See existing event pages to see how the parts are used
class Part(models.Model):
	header = models.CharField(max_length = 75,verbose_name="Title")
	body = RichTextField(verbose_name="Short Blurb/Description")
	image = models.ImageField(upload_to="conventions")
	convention = models.ForeignKey(Convention, on_delete = models.CASCADE,verbose_name="Linked Convention")
	def save(self):
		self.image = compress(self.image)
		super(Part, self).save()
	def __str__(self):
		return self.header
	class Meta:
		verbose_name="Convention Part"
		verbose_name_plural="Convention Parts"
class List(models.Model): #fundraisers and stuff (Note: this website pulls data off of the fudnraiser's facebook page, so be sure to make sure the API itself is working)
	name = models.CharField(max_length = 100, blank=True,verbose_name="Name of Fundraiser")
	url = models.CharField(max_length=1000,verbose_name="Link to Event FB Page")
	posts = models.ManyToManyField(Post, blank=True, related_name = "posts",verbose_name="Related WEBSITE Posts made about Event")
	desc = models.TextField(blank=True,verbose_name="Event Description")
	start_time = models.DateTimeField(blank=True, null=True)
	end_time = models.DateTimeField(blank=True, null = True)
	location = models.CharField(max_length=100, blank=True)
	slug = models.SlugField(blank=True)
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('events:event_detail', kwargs = {'list_id':self.id, 'slug':self.slug})	
	#mop up this area and eliminate the end time model
	def save(self):
		try:
			event_json = event_query(get_event_id(self.url)) 
			self.name = event_json['name']
			self.desc = event_json['description']
			self.start_time = parse(event_json['start_time'])
			try:
				self.end_time = parse(event_json['end_time'])
			except KeyError:
				pass
			self.location = event_json['place']['name']
		except requests.exceptions.HTTPError:
			pass
		self.slug = slugify(self.name)
		super(List, self).save()
	class Meta:
		verbose_name="Fundraiser"
		verbose_name_plural="Fundraisers"
#Table for Divisional Service Events
#Fun Fact: This was the first table which implemented automatic website updating and API usage
#You shouldn't ever need to manually update a Service EVent from the Django admin page, as the API automatically updates events for you.
class Service(models.Model):
	event_id = models.CharField(max_length=100)
	title = models.CharField(max_length=300)
	school = models.CharField(max_length=300)
	location = models.CharField(max_length=300)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	all_day = models.BooleanField()
	description = models.TextField()
	delete_time = models.DateTimeField(blank=True, null=True)
	update_time = models.DateTimeField(blank=True,null=True)
	slug = models.SlugField(max_length=300,blank=True)
	def __str__(self):
		return self.title
	def save(self):
		self.slug = slugify(self.title)
		super(Service, self).save()
	def get_absolute_url(self):
		return reverse('events:service_detail', kwargs = {'service_id':self.id, 'slug': self.slug})
	class Meta:
		verbose_name="Service Event"
		verbose_name_plural="Service Events"
#Create your models here.
