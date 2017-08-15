from blog.image_compress import compress
from django.template.defaultfilters import slugify
from django.db import models
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField
from django.core.urlresolvers import reverse
class Level(models.Model):
	key_level = models.CharField('Level of Key Club?', max_length = 100)
	name = models.CharField('Name of Project', max_length=100)
	logo = models.ImageField(upload_to='projects/')
	bkgnd_photo = models.ImageField(upload_to='projects/')
	def_short = RichTextField()
	video = EmbedVideoField()
	extend_desc = RichTextField()
	fundrs_goal = models.IntegerField('Fundraising Goal')
	slug = models.SlugField()
	def __str__(self):
		return self.key_level
	def get_absolute_url(self):
		return reverse('projects:detail',kwargs={'level_id':self.id,'slug':self.slug,})
	def save(self):
		self.logo = compress(self.logo)
		self.bkgnd_photo = compress(self.bkgnd_photo)
		self.slug = slugify(self.name)
		super(Level, self).save()
# Create your models here.
