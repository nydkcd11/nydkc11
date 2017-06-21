from django.conf.urls import url

from . import views
app_name = 'resources'
urlpatterns = [
	url(r'^videos/$',views.videos,name='videos'),
	url(r'^newsletter/$',views.newsletter,name='newsletter'),
	url(r'^minutes/$', views.minutes,name='minutes'),
]
