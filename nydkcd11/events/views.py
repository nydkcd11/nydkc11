from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import DTC, List
from blog.models import Post
def index(request):
	return HttpResponse("This is the events root page")
def dtc(request):
	dtc = DTC.objects.get(pk=1)
	return render(request, 'events/events.html',{'dtc':dtc})
def event_list(request):
	roster = List.objects.all()
	return render(request, 'events/list.html', {'roster':roster})
def event_detail(request, list_id):
	event = get_object_or_404(List, pk=list_id)
	links = []
	for post in event.posts.all():
		for link in post.link_set.all():
			links.append(link)
	posts = event.posts.all()
	return render(request, 'events/detail.html',{'event':event,'links':links,'posts':posts})
# Create your views here.
