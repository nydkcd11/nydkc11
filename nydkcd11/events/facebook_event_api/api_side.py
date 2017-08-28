import requests
import json
import pprint
PERM_TOKEN = 'EAAHyGRmpkT8BACTeK1cKXS8142tkBWExYGavMb8BUff775CgvplF3OPZA9SSDpTHb3jXFEw3wmwFvxjklZAnOG8TQMVVotgCYqzqCpiSx5cRUvx0oz00P4UZAglZADScfuXYlInZBfMaTCAPDd3LTgK1VAELXI5NzN1b2yZCsm7QZDZD'
HEADERS = {'access_token':PERM_TOKEN}
def event_query():
	event_id=111978872808697
	request = requests.get('https://graph.facebook.com/v2.10/%s' %(event_id), params=HEADERS)	
	if(request.ok):
		request_lib = json.loads(request.content)
		pprint.pprint(request_lib)
	else:
		request.raise_for_status()
#used to gain access to permanent token.
def long_access():
	payload = {
		'grant_type':'fb_exchange_token',	
		'client_id':'547664595358015',
		'client_secret':'6fe22820d18b1a79af44b6b66764335d',
		'fb_exchange_token':'EAAHyGRmpkT8BAOvVTnn1uLXcRQu0XNNwFqiBwuM37AZBobdtv18yf3TOp5f5YaWsS3T11cg1ZA9K5SMQHkeW8XnWrlnorELguhjEnlamnWQZCwqJElmLcTKKLGaZBhD9FZBdYo54iUPEkZBi89RR5ebwxYjFZCTlr1DJ5NgljNck4BHhEeNQxL9ooV9zjc6QahAuOIUW8mR9QZDZD',
	}
	request = requests.get('https://graph.facebook.com/v2.10/oauth/access_token', params=payload)
	if(request.ok):
		request_lib = json.loads(request.content)
		pprint.pprint(request_lib)
	else:
		request.raise_for_status()
def perm_access():
	payload = {
		'access_token':'EAAHyGRmpkT8BACEibJk055S6DdltCicOjXKPyzimXkkjruan3rRzJtwHjoXkK56WNu5KJ7LFGKv3DoHnwSUE2weZCyPRdyZBz3Y9UFDZBLRV4INrUIk9v6MSplzoeh4OTwEfuC7dHZBjUcsBcBBmaaPjlyKHkZBdpAJGAekU86AZDZD',
	}
	request = requests.get('https://graph.facebook.com/v2.10/me/accounts',params = payload)
	if(request.ok):
		request_lib = json.loads(request.content)
		pprint.pprint(request_lib)
	else:
		request.raise_for_status()

