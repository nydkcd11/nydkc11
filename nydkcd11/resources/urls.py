from django.conf.urls import url

from . import views
app_name = 'resources'
urlpatterns = [
	url(r'^videos/$',views.videos,name='videos'),
	url(r'^minutes/$', views.minutes,name='minutes'),
	url(r'^gallery/$', views.gallery, name = 'gallery'),
	url(r'^gallery/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$', views.gallery_specific, name = 'gallery_specific')
]
