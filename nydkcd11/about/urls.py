from django.conf.urls import url
from . import views
app_name = 'about'
urlpatterns = [
	url(r'^division/$',views.division,name='division'),
	url(r'^clubs/$', views.clubs, name = 'clubs'),	
	url(r'^faq/$', views.faq, name = 'faq'),
]
