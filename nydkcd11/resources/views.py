from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Link,Video
def index(request):
	video_list = Video.objects.all()
	link_list=Link.objects.all()
	context = {
		'video_list':video_list,	
		'link_list':link_list,
	}
	return render(request,'resources/index.html',context)
def videos(request):
	video_list = Video.objects.all()
	context = {
		'video_list':video_list,	
	}
	return render(request,'resources/videos.html',context)
def links(request):
	link_list = Link.objects.all()
	context = {
		'link_list':link_list,	
	}
	return render(request,'resources/links.html', context)
# Create your views here.
