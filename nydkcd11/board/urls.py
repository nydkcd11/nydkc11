from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^divisional/$', views.index, name = 'index'),
	#url(r'^(?P<person_id>[0-9]+)/$', views.results, name = "results"), #temp
]
