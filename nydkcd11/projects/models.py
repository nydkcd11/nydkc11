from blog.image_compress import compress
from django.template.defaultfilters import slugify
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from embed_video.fields import EmbedVideoField
from django.core.urlresolvers import reverse
#DB for various projects the division/KC does
class Level(models.Model):
	key_level = models.CharField('Level of Key Club?', max_length = 100)
	name = models.CharField('Name of Project', max_length=100)
	logo = models.ImageField(upload_to='projects/',verbose_name="Logo of Organization")
	bkgnd_photo = models.ImageField(upload_to='projects/',verbose_name="Background Photo")
	def_short2 = RichTextUploadingField(verbose_name="Short Description of Organization")
	video = EmbedVideoField(verbose_name="Video of Organization")
	extend_desc2 = RichTextUploadingField(verbose_name="Extensive Description")
	fundrs_goal = models.IntegerField('Fundraising Goal')
	slug = models.SlugField(blank=True)
	def __str__(self):
		return self.key_level
	def get_absolute_url(self):
		return reverse('projects:detail',kwargs={'level_id':self.id,'slug':self.slug,})
	def save(self):
		self.logo = compress(self.logo)
		self.bkgnd_photo = compress(self.bkgnd_photo)
		self.slug = slugify(self.name)
		super(Level, self).save()
	class Meta:
		verbose_name = "Key Club Project"
		verbose_name_plural= "Key Club Projects"
# Create your models here.
