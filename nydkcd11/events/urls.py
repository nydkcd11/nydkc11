from django.conf.urls import url
from . import views
app_name = 'events'
urlpatterns= [
	url(r'^$', views.index, name = 'index'),	
	url(r'^dtc/$', views.dtc, name = 'dtc'),
]
 
