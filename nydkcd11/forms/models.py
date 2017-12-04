from django.db import models
#Resources (e.g. the MRF Form)
#don't ask why this has its own table
class Papers(models.Model):
	name = models.CharField(max_length = 30,verbose_name="Title of Paper/Form/Application")
	url = models.CharField(max_length = 300,verbose_name="URL to Paper/Form/Application") 
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "Application Resource"
		verbose_name = "Application Resources"
# Create your models here.
