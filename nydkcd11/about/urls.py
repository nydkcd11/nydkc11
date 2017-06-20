from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$',views.index, name = 'index'),
	url(r'^division/$',views.division,name='division'),
	url(r'^clubs/$', views.clubs, name = 'clubs'),	
]
