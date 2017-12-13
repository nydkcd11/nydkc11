#urls page for about -- maps request to appropriate page point
from django.conf.urls import url
from . import views
app_name = 'about' #be sure to include app_name in future apps
urlpatterns = [
	url(r'^division/$',views.division,name='division'),
	url(r'^clubs/$', views.clubs, name = 'clubs'),	
	url(r'^faq/$', views.faq, name = 'faq'),
	url(r'^', views.index, name = "index"),
]
