from django.db import models
from blog.models import Post
class Newsletter(models.Model):
	post = models.ForeignKey(Post, on_delete = models.CASCADE,verbose_name = "Linked Post")
	month = models.CharField(max_length = 30,verbose_name="Month of Newsletter")
	url = models.CharField(max_length=100,verbose_name="Link to Issuu")
	def __str__(self):
		return str(self.month)
class Minutes(models.Model):
	post = models.ForeignKey(Post, on_delete = models.CASCADE,verbose_name = "Linked Post")
	location = models.CharField(max_length=50, default = "Division 11",verbose_name = "Place where Divisional was Held")
	month = models.DateField(verbose_name = "Month of Divisional")
	notes = models.FileField(upload_to = 'minutes/',verbose_name = "Minutes File")
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
	class Meta:
		verbose_name= "Minute"
		verbose_name_plural = "Minutes"
	
	
# Create your models here.
