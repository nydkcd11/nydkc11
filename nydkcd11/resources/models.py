from django.db import models
class Newsletter(models.Model):
	month = models.CharField(max_length = 30)
	url = models.CharField(max_length=100)
	def __str__(self):
		return str(self.month)
class Minutes(models.Model):
	month = models.DateField()
	url = models.CharField(max_length=100)
	def january():
		return "January"
	def february():
		return "February"
	def march():
		return "March"
	def april():
		return "April"
	def may():
		return "May"
	def june():
		return "June"
	def july():
		return "July"
	def august():
		return "August"
	def september():
		return "September"
	def october():
		return "October"
	def november():
		return "November"
	def december():
		return "December"
	def __str__(self):
		options = {
			1:"January",
			2:"february",
			3:"march",
			4:"april",
			5:"may",
			6:"june",
			7:"july",
			8:"august",
			9:"september",
			10:"october",
			11:"november",
			12:"december",	
		}
		number = self.month.month
		return options[number]()

	
	
# Create your models here.
