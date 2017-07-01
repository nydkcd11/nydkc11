from django.conf.urls import url

from . import views
app_name = 'contact'
urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^thanks/$',views.done, name = 'done'),
	url(r'^email_process/$',views.email_process, name= 'email_process'),
]
