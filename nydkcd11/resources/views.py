from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Video
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
	return HttpResponse("newsletter")
def minutes(request):
	return HttpResponse("minutes")
# Create your views here.
