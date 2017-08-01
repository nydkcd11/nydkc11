#deal with editing events problemn
#note: this command should be run ONCE per day (24 hours), via a chrontab job
from events.models import Service
from django.core.management.base import BaseCommand, CommandError
from events.teamup_api.mid_side import daily_query
from datetime import datetime
class Command(BaseCommand):
	help = 'downloads events created, changed, or deleted and pushes updates onto the database'
	def handle(self, *args, **options):
		test =  daily_query() 
		if len(test) == 0:
			self.stdout.write(self.style.ERROR("No events were created, changed, or deleted recently."))
		else:
			existing_ids = []
			for event in Service.objects.all():
				 existing_ids.append(event.event_id)
			for service in test:
				print(type(service.delete_time))
				if service.event_id not in existing_ids and service.delete_time is None: 
					service.save()
					self.stdout.write(self.style.SUCCESS("The event %s was succesfully pushed to the database" %(service.title)))
				elif service.delete_time is not None:
					Service.objects.filter(event_id=service.event_id).delete()
					self.stdout.write(self.style.SUCCESS("The event %s was succesfully deleted from the database" %(service.title)))
				else:
					Service.objects.filter(event_id=service.event_id).delete()
					service.save()
					self.stdout.write(self.style.SUCCESS("The event %s was succesfully updated to the database" %(service.title)))
