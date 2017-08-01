from events.models import Service
from django.core.management.base import BaseCommand, CommandError
from events.teamup_api.mid_side import dates
from datetime import datetime
class Command(BaseCommand):
	help = 'downloads events within date range and posts them onto API. NOTE: change date settings inside manual_update.py'
	def handle(self, *args, **options):
		start = datetime(2017,7,28)
		end = datetime(2017,8,19)
		test = dates(start,end)
		existing_ids = []
		for event in Service.objects.all():
			 existing_ids.append(event.event_id)
		print(existing_ids)
		for service in test:
			if service.event_id not in existing_ids: 
				service.save()
				self.stdout.write(self.style.SUCCESS("The event %s was succesfully pushed to the database" %(service.title)))
			else:
				self.stdout.write(self.style.ERROR("The event %s was not pushed because it's already in the database" %(service.title)))
