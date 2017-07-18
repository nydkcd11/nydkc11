from django.db import models
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField
class Level(models.Model):
	key_level = models.CharField('Level of Key Club?', max_length = 100)
	name = models.CharField('Name of Project', max_length=100)
	logo = models.ImageField(upload_to='projects/')
	bkgnd_photo = models.ImageField(upload_to='projects/')
	def_short = RichTextField()
	video = EmbedVideoField()
	extend_desc = RichTextField()
	fundrs_goal = models.IntegerField()
	hours_goal = models.IntegerField()
	def __str__(self):
		return self.key_level
# Create your models here.
