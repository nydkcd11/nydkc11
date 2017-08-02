from projects.colorgen import hexgen
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import DTC, List, Convention, Part, Service
from blog.models import Post
def dtc(request):
	dtc = DTC.objects.get(pk=1)
	return render(request, 'events/events.html',{'dtc':dtc})
def event_list(request):
	roster = List.objects.order_by('-pk')
	return render(request, 'events/list.html', {'roster':roster})
def event_detail(request, list_id, slug):
	event = get_object_or_404(List, pk=list_id)
	links = []
	for post in event.posts.all():
		for link in post.link_set.all():
			links.append(link)
	#needs fixing atm
	images = []
	for post in event.posts.all():
		for image in post.image_set.all():
			images.append(image)
	videos = []
	for post in event.posts.all():
		for video in post.video_set.all():
			videos.append(video)
	if event.slug != slug:
		return redirect('events:event_detail', slug = event.slug, list_id = event.id)
	return render(request, 'events/detail.html',{'event':event,'links':links,'images':images,'videos':videos})
def event_redirect(request, list_id):
	event = get_object_or_404(List, pk = list_id)
	return redirect('events:event_detail',slug = event.slug, list_id = event.id)
def long_event(request, convention_id):
	convention = get_object_or_404(Convention, pk = convention_id)
	color = []
	sections = convention.part_set.all()
	for section in convention.part_set.all():
		color.append(hexgen())
	colors = zip(sections, color)
	mobile_color = hexgen()
	color_2 = hexgen()
	return render(request, 'events/long_event.html', {'convention':convention,'colors':colors, 'mobile_color':mobile_color, 'color_2':color_2})
def service_events(request):
	services = Service.objects.all()
	return render(request, 'events/service_events.html', {'services':services})	
def service_detail(request, service_id):
	event = get_object_or_404(Service, pk= service_id)
	return render(request, 'events/service_detail.html', {'event':event})
# Create your views here.
