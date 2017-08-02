from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Image, Post, Article
from contact.forms import EmailForm
from events.models import Service
from django.utils import timezone
from datetime import timedelta
def index(request):
	image_master = Image.objects.order_by('-post') #need way to sort by pub_date from post
	image_list = []
	for image in image_master:
		if image.show_home==True:
			image_list.append(image)
	image_list = image_list[:7]
	length = []
	for i in range(len(image_list)):
		length.append(i)
	blog_list = Post.objects.order_by('pub_date_2').reverse()[:4]
	#article_list = Article.objects.order_by('-pk')[:4]
	start_date = timezone.now().date()
	end_date = start_date + timedelta(days=365)
	article_list = Service.objects.filter(start_time__range=(start_date,end_date))[0:4]
	return render(request, 'nydkcd11/home.html',{'image_list':image_list,'length':length, 'blog_list':blog_list,'article_list':article_list})
