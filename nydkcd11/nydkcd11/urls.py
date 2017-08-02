"""nydkcd11 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from django.conf import settings
from django.conf.urls.static import static
from . import views
from sitemaps import *
from blog.models import Post, Article
from events.models import List, Service, Convention
from projects.models import Level
convention_dict = {
	'queryset':Convention.objects.all()	
}
service_dict = {
	'queryset':Service.objects.all()	
}
level_dict = {
	'queryset':Level.objects.all()	
}
post_dict={
	'queryset':Post.objects.all()	
}

article_dict={
	'queryset':Article.objects.all()	
}
event_dict={
	'queryset':List.objects.all()	
}
sitemaps = {
	'convention':GenericSitemap(convention_dict),
	'service':GenericSitemap(service_dict),
	'level':GenericSitemap(level_dict),
	'list':GenericSitemap(post_dict),
	'article':GenericSitemap(article_dict),
	'event':GenericSitemap(event_dict),
	'about':AboutSitemap(),
	'contact':ContactSitemap(),
	'resources':ResourcesSitemap(),
	'forms':FormsSitemap(),
	'events':EventsSitemap(),
	'blog':BlogSitemap(),
}
urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^about/', include('about.urls')),
	url(r'^admin/', admin.site.urls),
	url(r'^blog/', include('blog.urls')),
	url(r'^contact/', include('contact.urls')),
	url(r'^resources/', include('resources.urls')),
	url(r'^forms/', include('forms.urls')),
	url(r'^events/', include('events.urls')),
	url(r'^projects/', include('projects.urls')),
	url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap')
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
