from blog.image_compress import compress #self-made website utility that automatically processes images
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
#Database Table for Divisional Members
#Fun Fact: This was the very first database created for the website.
class Division(models.Model):
	name = models.CharField(max_length = 100)
	school = models.CharField(max_length = 75)
	email = models.CharField(max_length=75)
	position = models.CharField(max_length = 50)
	desc = models.TextField(verbose_name="About the Board Member")
	image = models.ImageField(upload_to='division_photos/',verbose_name="Board Member's Image")
	def __str__(self):
		return self.name
	def save(self, *args, **kwargs):
		self.image = compress(self.image) 
		super(Division,self).save()
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
	newsletter_url = models.URLField(max_length=300, default = "#",verbose_name="Newsletter Link")
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
	answer3 = RichTextUploadingField(verbose_name="Answer")
	def __str__(self):
		return self.question
# Create your models here.
