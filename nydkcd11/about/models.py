from blog.image_compress import compress
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
class Division(models.Model):
	name = models.CharField(max_length = 100)
	school = models.CharField(max_length = 75)
	email = models.CharField(max_length=75)
	position = models.CharField(max_length = 50)
	desc = models.TextField()
	image = models.ImageField(upload_to='division_photos/')
	def __str__(self):
		return self.name
	def save(self, *args, **kwargs):
		self.image = compress(self.image) 
		super(Division,self).save()
class School(models.Model):
	school = models.CharField(max_length = 100)
	pres = models.CharField(max_length = 75, default = "N/A")
	pres_email = models.CharField('President\'s Email', max_length=75)
	vicepres = models.CharField(max_length = 75, default = "N/A")
	vp_email = models.CharField('Vice President\'s Email',max_length=75)
	secretary = models.CharField(max_length = 75, default = "N/A")
	secret_email = models.CharField('Secretary\'s Email', max_length = 75)
	treasurer = models.CharField(max_length = 75, default = "N/A")
	treas_email = models.CharField('Treasurer\'s Email',max_length = 75)
	webmaster = models.CharField(max_length = 75, default = "N/A")
	webm_email = models.CharField('Webmaster\'s Email',max_length=75)
	editor = models.CharField(max_length = 75, default = "N/A")
	editor_email = models.CharField('Editor\'s Email', max_length=75)
	url = models.CharField(max_length = 300, default = "#")
	newsletter_url = models.URLField(max_length=300, default = "#")
	image = models.ImageField(upload_to='school_photos/')
	def __str__(self):
		return self.school	
	def save(self, *args, **kwargs):
		self.image = compress(self.image)
		super(School, self).save()
class FAQ(models.Model):
	question = models.CharField(max_length = 300)
	answer2 = RichTextField()
	answer3 = RichTextUploadingField()
	def __str__(self):
		return self.question
# Create your models here.
