from django.db import models
#Note: only one object should be registered for all models here. 
class DTC(models.Model):
	title = models.CharField(max_length = 50)
	description = models.TextField() 
	image = models.ImageField(upload_to='dtc_event')
#Create your models here.
