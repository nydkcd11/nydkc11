from django.db import models
from embed_video.fields import EmbedVideoField
from django.core.urlresolvers import reverse
class Post(models.Model):
	title = models.CharField(max_length = 100)
	author = models.CharField(max_length = 50)
	pub_date_2 = models.DateField('publish date')
	body2 = models.TextField('Main Body of Text')
	blurb = models.CharField(max_length = 300)
	def __str__(self):
		return self.title
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	def get_absolute_url(self):
		return reverse('blog:detail',kwargs = {'post_id':self.id})
	class Meta:
		ordering = ['pub_date_2']
class Image(models.Model):
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	title = models.CharField(max_length = 1000)
	desc = models.CharField(max_length = 1000)
	image =  models.ImageField(upload_to='image_main/')
	show_home = models.BooleanField('Show in Home Page?', blank = True, default = False)
	def __str__(self):
		return self.title
class Video(models.Model):
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	video = EmbedVideoField()
	def __str__(self):
		return self.post.title
class Link(models.Model):
	link = models.ForeignKey(Post, on_delete = models.CASCADE, verbose_name = "Primary Post")
	other_link = models.ManyToManyField(Post, blank=True, related_name = "links", verbose_name = "Other Related Posts")
	name = models.CharField(max_length=30)
	url = models.CharField(max_length=1000)
	host = models.CharField(max_length = 50)
	DIVISION = 'DIV'
	FUNDRAISER = 'FUND'
	CLUB='CLUB'
	KIWANNIS = 'KWNS'
	EVENT_CHOICES = (
		(DIVISION,'Division Events'),
		(FUNDRAISER,'Fundraisers'),
		(CLUB, 'Club Events'),
		(KIWANNIS, 'Kiwannis Events'),
	)
	event_choices=models.CharField('Type of Event',max_length=4,choices=EVENT_CHOICES,default=FUNDRAISER)
	show_screen = models.BooleanField('Show on Events List?', blank=True, default=False)
	def __str__(self):
		return self.name
class Article(models.Model):
	title = models.CharField(max_length = 100)
	author = models.CharField(max_length = 50)
	date = models.CharField(max_length = 100)
	body = models.TextField()
	blurb = models.CharField(max_length = 300)
	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('blog:news', kwargs = {'article_id':self.id})
# Create your models here.
