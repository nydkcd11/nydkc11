from django.db import models

class Post(models.Model):
	title = models.CharField(max_length = 100)
	author = models.CharField(max_length = 50)
	pub_date = models.DateTimeField('date publshed')
	body = models.CharField(max_length = 10000)
	def __str__(self):
		return self.title
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
class Image(models.Model):
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	desc = models.CharField(max_length = 1000)
	#image =  models.ImageField()

class Video(models.Model):
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	url = models.CharField(max_length = 1000)
	def __str__(self):
		return self.post.title
	def parse(self):
		return 0
		#supposed to generate an iframe 
class Tag(models.Model):
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	name = models.CharField(max_length = 30)
# Create your models here.
