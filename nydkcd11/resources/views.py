from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Video
from .models import Newsletter, Minutes
def index(request):
	video_list = Video.objects.all()
	context = {
		'video_list':video_list,	
	}
	return render(request,'resources/index.html',context)
def videos(request):
	video_list = Video.objects.all()
	context = {
		'video_list':video_list,	
	}
	return render(request,'resources/videos.html',context)
def newsletter(request):
	newsletter_list = Newsletter.objects.all()
	return render(request,'resources/newsletter.html',{'newsletter_list':newsletter_list})
def minutes(request):
	minutes_list = Minutes.objects.all()
	return render(request,'resources/minutes.html',{'minutes_list':minutes_list})
# Create your views here.
