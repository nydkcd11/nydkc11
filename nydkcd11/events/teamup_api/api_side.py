#figure out way to get events only from subcalendar
import calendar
import time
import datetime
import requests
import json
HEADERS = {
	'Teamup-Token':'d1f0594a4a113ac17777700b8f429f5c17f89d06b9e25087357b391b39a7979b',	
}	
CALENDAR_KEY = 'ksgewfa61tnr5cckek'
SUB_CALENDAR = '3060119'
def day_query(year_start, month_start, day_start, year_end, month_end, day_end): #gets event range from certain period of time
	#date_start = str(time.mktime(datetime.datetime(year_start, month_start, day_start).timetuple()))[:-2]
	#date_end = str(time.mktime(datetime.datetime(year_end, month_end, day_end).timetuple()))[:-2]
	date_start = datetime.datetime(year_start, month_start, day_start)
	date_end = datetime.datetime(year_end, month_end, day_end)
	payload = {
		'startDate': date_start,
		'endDate': date_end,	
	}
	#print(str(date_start) + "\n" + str(date_end))
	request = requests.get('https://api.teamup.com/%s/events' % (CALENDAR_KEY), params = payload, headers = HEADERS)
	#request = requests.get('https://api.teamup.com/%s/subcalendars/%s/events' % (CALENDAR_KEY, SUB_CALENDAR), params = payload, headers = HEADERS)
	if(request.ok):
		request_lib = json.loads(request.content)
		del request_lib['timestamp']
		return request_lib
	else:
		request.raise_for_status()

def id_query(event_num): #queries specific event
	request = requests.get('https://api.teamup.com/%s/events/%s' % (CALENDAR_KEY, str(event_num),), headers = HEADERS)
	if (request.ok): #integrate into model later?
		request_lib = json.loads(request.content)['event']
		'''
		request_lib = {
			'id':request_lib['id'],
			'start_dt':request_lib['start_dt'],
			'end_dt':request_lib['end_dt'],
			'all_day':request_lib['all_day'],
			'title':request_lib['title'],
			#and so on
		}
		'''
		return request_lib
	else:
		request.raise_for_status()
def event_update(): #queries recent changes
	present = datetime.datetime.now()
	payload = {
		'modifiedSince': str(time.mktime(datetime.datetime(present.year, present.month, present.day, 0,0,0).timetuple()))[:-2],	
	}
	#print(int(time.time()))
	request = requests.get('https://api.teamup.com/%s/events' % (CALENDAR_KEY,), params = payload, headers = HEADERS)
	if (request.ok):
		request_lib = json.loads(request.content)
		del request_lib['timestamp']
		print(request_lib)
		return request_lib
	else:
		request.raise_for_status()
	
