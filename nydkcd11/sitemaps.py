from django.contrib.sitemaps import Sitemap
from about.urls import urlpatterns as aboutURLs
from contact.urls import urlpatterns as contactURLs
from resources.urls import urlpatterns as resourcesURLs
from forms.urls import urlpatterns as formsURLs
from events.urls import urlpatterns as eventsURLs
from blog.urls import urlpatterns as blogURLs
from django.core.urlresolvers import reverse
class AboutSitemap(Sitemap):
	def items(self):
		url_list = []
		for url in aboutURLs:
			url_list.append('about:'+url.name)
		return url_list
	def location(self,item):
		return reverse(item)	
class ContactSitemap(Sitemap):
	def items(self):
		url_list = []
		for url in contactURLs:
			url_list.append('contact:'+url.name)
		return url_list
	def location(self,item):
		return reverse(item)	
class ResourcesSitemap(Sitemap):
	def items(self):
		url_list = []
		for url in resourcesURLs:
			url_list.append('resources:'+url.name)
		return url_list
	def location(self,item):
		return reverse(item)	
class FormsSitemap(Sitemap):
	def items(self):
		url_list = []
		for url in formsURLs:
			url_list.append('forms:'+url.name)
		return url_list
	def location(self,item):
		return reverse(item)	
class EventsSitemap(Sitemap):
	def items(self):
		url_list = []
		for url in eventsURLs:
			if url.name != 'event_detail' and url.name != 'event_redirect' and url.name != 'service_detail' and url.name != 'service_redirect' and url.name != 'long_event' and url.name != 'long_event_redirect':
				url_list.append('events:'+url.name)
		return url_list
	def location(self,item):
		return reverse(item)
class BlogSitemap(Sitemap):
	def items(self):
		url_list = []
		for url in blogURLs:
			if url.name != 'detail' and url.name != 'news' and url.name != 'news_redirect' and url.name != 'detail_redirect':
				url_list.append('blog:'+url.name)
		return url_list
	def location(self, item):
		return reverse(item) 
