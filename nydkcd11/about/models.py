#Models.py for About App
#defines generel table schema for About's database
#You don't design actual schema, but it's autogenereated from the Python classes
#Look on Django's documentation for a full explanation of what a model is
from blog.image_compress import compress #self-made website utility that automatically processes images
from django.db import models
#stuff from Ckeditor, a rich text editor implemented for the website
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
#Database Table for Divisional Members
#Fun Fact: This was the very first database created for the website.
class Division(models.Model):
	name = models.CharField(max_length = 100) #charfields are text fields with limits
	school = models.CharField(max_length = 75)
	email = models.CharField(max_length=75)
	position = models.CharField(max_length = 50)
	desc = models.TextField(verbose_name="About the Board Member") #textfields are text fields without limits. verbose names tell Python to rename it on the Django Admin
	image = models.ImageField(upload_to='division_photos/',verbose_name="Board Member's Image") #imagefields host server images. 
	#note: images are handled differently in prod and dev. look it up on django's documentation.

	#returns name for admin usage
	def __str__(self):
		return self.name

	#implementaiton of compress method (image optimization)
	def save(self, *args, **kwargs):
		self.image = compress(self.image) 
		super(Division,self).save()
	#more admin stuff 
	class Meta:
		verbose_name = "Divisional Board Member"
		verbose_name_plural = "Divisional Board Members"
#Table for School Clubs
class School(models.Model):
	school = models.CharField(max_length = 100)
	pres = models.CharField(max_length = 75, default = "N/A",verbose_name="President")
	pres_email = models.CharField('President\'s Email', max_length=75)
	vicepres = models.CharField(max_length = 75, default = "N/A",verbose_name="Vice President")
	vp_email = models.CharField('Vice President\'s Email',max_length=75)
	secretary = models.CharField(max_length = 75, default = "N/A")
	secret_email = models.CharField('Secretary\'s Email', max_length = 75)
	treasurer = models.CharField(max_length = 75, default = "N/A")
	treas_email = models.CharField('Treasurer\'s Email',max_length = 75)
	webmaster = models.CharField(max_length = 75, default = "N/A")
	webm_email = models.CharField('Webmaster\'s Email',max_length=75)
	editor = models.CharField(max_length = 75, default = "N/A")
	editor_email = models.CharField('Editor\'s Email', max_length=75)
	url = models.CharField(max_length = 300, default = "#",verbose_name="Club Website")
	newsletter_url = models.URLField(max_length=300, default = "#",verbose_name="Newsletter Link") #URL verification
	image = models.ImageField(upload_to='school_photos/',verbose_name = "School Logo")
	def __str__(self):
		return self.school	
	def save(self, *args, **kwargs):
		self.image = compress(self.image)
		super(School, self).save()
	class Meta:
		verbose_name = "School Club"
		verbose_name_plural = "School Clubs"
#Table for FAQ questions page
#Fun Fact: This was the first table to implement ckeditor
class FAQ(models.Model):
	question = models.CharField(max_length = 300)
	answer3 = RichTextUploadingField(verbose_name="Answer") #instead of plain text, you get rich text !!!
	def __str__(self):
		return self.question
# Create your models here.
