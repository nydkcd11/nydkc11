from django.template.defaultfilters import slugify
from django.db import models
from embed_video.fields import EmbedVideoField
from django.urls import reverse
from blog.image_compress import compress
class Post(models.Model):
	title = models.CharField(max_length = 100)
	author = models.CharField(max_length = 50)
	pub_date_2 = models.DateField('publish date')
	body2 = models.TextField('Main Body of Text')
	blurb = models.CharField(max_length = 300,verbose_name="Short Summary of Post")
	slug = models.SlugField(blank=True)
	def __str__(self):
		return self.title
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	def get_absolute_url(self):
		return reverse('blog:detail',kwargs = {'post_id':self.id, 'slug':self.slug})
	def save(self):
		self.slug = slugify(self.title)
		super(Post, self).save()
	class Meta:
		ordering = ['pub_date_2']

#Primary Database for Images
#Possible Project: Automatically import images from Divisional Photo Drive?	
class Image(models.Model):
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	other_post = models.ManyToManyField(Post, blank=True, related_name = "image_posts", verbose_name = "Other Linked Posts")
	title = models.CharField(max_length = 1000,verbose_name="Image Title")
	desc = models.CharField(max_length = 1000,verbose_name="Short Image Description")
	image =  models.ImageField(upload_to='image_main/')
	show_home = models.BooleanField('Show in Home Page?', blank = True, default = False)
	def __str__(self):
		return self.title
	def save(self, *args, **kwargs):
		self.image = compress(self.image)
		super(Image,self).save()		
		
class Video(models.Model):
	post_related = models.ManyToManyField(Post, blank = True, related_name = "video_posts", verbose_name = "Other Related Posts")
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	video = EmbedVideoField()
	def __str__(self):
		return self.post.title
class Link(models.Model):
	link = models.ForeignKey(Post, on_delete = models.CASCADE, verbose_name = "Primary Post")
	other_link = models.ManyToManyField(Post, blank=True, related_name = "links", verbose_name = "Other Related Posts")
	name = models.CharField(max_length=30)
	url = models.CharField(max_length=1000,verbose_name="Signup Sheet/Link")
	host = models.CharField(max_length = 50,verbose_name="Hosting School/Organization")
	#options for dropdown menu on django admin page. This eventually gets processed in the front-end
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
	body = models.TextField(verbose_name="Body of Article")
	blurb = models.CharField(max_length = 300,verbose_name="Short Summary of Article")
	slug = models.SlugField(blank=True) #this enables contextualized link generation in the URL
	def __str__(self):
		return self.title
	def get_absolute_url(self): #gets a linkage from the article for sitemap purposes
		return reverse('blog:news', kwargs = {'article_id':self.id, 'slug':self.slug})
	def save(self):
		self.slug = slugify(self.title)
		super(Article, self).save()
# Create your models here.
