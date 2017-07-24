from django.conf.urls import url
from . import views
app_name = 'blog'
urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^article/$', views.article, name = 'article'),
	url(r'^(?P<post_id>[0-9]+)/$', views.detail, name = 'detail'),
	url(r'^article/(?P<article_id>[0-9]+)/$', views.news_redirect, name = 'news_redirect'),
	url(r'^article/(?P<article_id>[0-9]+)/(?P<slug>[\w-]+)/$', views.news, name = 'news'),

]
