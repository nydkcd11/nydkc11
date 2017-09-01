from django.db import models
from blog.models import Post
class Newsletter(models.Model):
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	month = models.CharField(max_length = 30)
	url = models.CharField(max_length=100)
	def __str__(self):
		return str(self.month)
class Minutes(models.Model):
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	location = models.CharField(max_length=50, default = "Division 11")
	month = models.DateField()
	notes = models.FileField(upload_to = 'minutes/')
	def __str__(self):
		options = {
			1:"January",
			2:"February",
			3:"March",
			4:"April",
			5:"May",
			6:"June",
			7:"July",
			8:"August",
			9:"September",
			10:"October",
			11:"November",
			12:"December",	
		}
		number = self.month.month
		return options[number] + " Divisional Notes"

	
	
# Create your models here.
