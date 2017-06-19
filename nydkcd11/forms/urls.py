from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^papers/$',views.papers, name = 'papers'),
	url(r'^signup/$',views.signup, name = 'signup'),
]
