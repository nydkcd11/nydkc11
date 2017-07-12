from django.conf.urls import url
from . import views
app_name = 'events'
urlpatterns= [
	url(r'^$', views.index, name = 'index'),	
	url(r'^dtc/$', views.dtc, name = 'dtc'),
	url(r'^event_list/$', views.event_list, name = 'event_list'),
	url(r'^(?P<list_id>[0-9]+)/$', views.event_detail, name = 'event_detail')
]
 
