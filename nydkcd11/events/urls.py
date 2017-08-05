from django.conf.urls import url
from . import views
app_name = 'events'
urlpatterns= [
	url(r'^dtc/$', views.dtc, name = 'dtc'),
	url(r'^event_list/$', views.event_list, name = 'event_list'),
	url(r'^event_list/(?P<list_id>[0-9]+)/(?P<slug>[\w-]+)/$', views.event_detail, name = 'event_detail'),
	url(r'^event_list/(?P<list_id>[0-9]+)', views.event_redirect, name = 'event_redirect'),
	url(r'^long_event/(?P<convention_id>[0-9]+)/$', views.long_event, name = 'long_event'),
	url(r'^service_events/$', views.service_events, name = 'service_events'),
	url(r'^service_events/(?P<service_id>[0-9]+)/(?P<slug>[\w-]+)/$', views.service_detail, name = 'service_detail'),
	url(r'^service_events/(?P<service_id>[0-9]+)/$', views.service_redirect, name = 'service_redirect')
]
 
