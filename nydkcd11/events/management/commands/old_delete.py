from django.utils import timezone
from events.models import Service
from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
class Command(BaseCommand):
	help = 'sees if any dates are old and deletes them'
	def handle(self, *args, **options):
		now = timezone.now() 
		for service in Service.objects.all():	
			if service.start_time < now:
				self.stdout.write(self.style.SUCCESS("The event %s was successfully deleted from the database" %(service.title)))
				service.delete()
		self.stdout.write("All other events are past %s/%s/%s" %(now.month, now.day, now.year))
