#fix fundraiser parse out
from dateutil.parser import parse
from events.models import Service 
import datetime
from .api_side import *
import pprint
def none_parse(phrase):
	if phrase is None or phrase == "":
		return "N/A"
	else:
		return phrase
def object_create(event_list):
	service_objects = []
	for event in event_list:
		temp = Service(
			event_id = event['id'],
			title=event['title'],
			school=none_parse(event['who']),
			location=none_parse(event['location']),
			start_time=parse(event['start_dt']),
			end_time=parse(event['end_dt']),
			all_day=event['all_day'],
			description=none_parse(event['notes'])
		)
		if event['delete_dt'] is not None: #need clarification on what's delete_dt default
			temp.delete_time = parse(event['delete_dt'])
		print(type(temp.delete_time))
		service_objects.append(temp)
	return service_objects
def dates(start,end):
	event_list = day_query(start.year, start.month, start.day, end.year, end.month, end.day)['events']
	service_objects = object_create(event_list)
	return service_objects
def daily_query():
	event_list = event_update()['events']
	print(event_list)
	service_objects = object_create(event_list)
	return service_objects
