from django.db import models
from embed_video.fields import EmbedVideoField
class Post(models.Model):
	title = models.CharField(max_length = 100)
	author = models.CharField(max_length = 50)
	pub_date = models.DateTimeField('date publshed')
	body2 = models.TextField('Main Body of Text')
	blurb = models.CharField(max_length = 300)
	def __str__(self):
		return self.title
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
class Image(models.Model):
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	title = models.CharField(max_length = 1000)
	desc = models.CharField(max_length = 1000)
	image =  models.ImageField(upload_to='image_main/')
	def __str__(self):
		return self.title
class Video(models.Model):
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	video = EmbedVideoField()
	def __str__(self):
		return self.post.title
class Link(models.Model):
	link = models.ForeignKey(Post, on_delete = models.CASCADE)
	name = models.CharField(max_length=30)
	url = models.CharField(max_length=1000)
	host = models.CharField(max_length = 50)
	DIVISION = 'DIV'
	FUNDRAISER = 'FUND'
	CLUB='CLUB'
	EVENT_CHOICES = (
		(DIVISION,'Division Events'),
		(FUNDRAISER,'Fundraisers'),
		(CLUB, 'Club Events'),
	)
	event_choices=models.CharField(max_length=4,choices=EVENT_CHOICES,default=FUNDRAISER)
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
# Create your models here.
