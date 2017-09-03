from projects.colorgen import hexgen
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import List, Convention, Part, Service
from blog.models import Post
from datetime import timedelta
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.page import page
def event_list(request):
	roster = List.objects.order_by('-start_time')
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
def long_event(request, convention_id, slug):
	convention = get_object_or_404(Convention, pk = convention_id)
	color = []
	sections = convention.part_set.all()
	for section in convention.part_set.all():
		color.append(hexgen())
	colors = zip(sections, color)
	mobile_color = hexgen()
	color_2 = hexgen()
	if slug != convention.slug:
		return redirect('events:long_event', slug = convention.slug, convention_id = convention.id)
	return render(request, 'events/long_event.html', {'convention':convention,'colors':colors, 'mobile_color':mobile_color, 'color_2':color_2})
def long_event_redirect(request, convention_id):
	convention = get_object_or_404(Convention, pk = convention_id)
	return redirect('events:long_event', slug = convention.slug, convention_id = convention.id)
def service_events(request):
	start_date = timezone.now().date()	
	end_date = start_date + timedelta(days=365)
	services = Service.objects.order_by('start_time').filter(start_time__range=(start_date,end_date))
	posts = page(services,request)
	return render(request, 'events/service_events.html', {'posts':posts})	
def service_detail(request, service_id, slug):
	event = get_object_or_404(Service, pk= service_id)
	if event.slug != slug:
		return redirect('events:service_detail', slug = event.slug, service_id = event.id)
	return render(request, 'events/service_detail.html', {'event':event})
def service_redirect(request, service_id):
	event = get_object_or_404(Service, pk = service_id)
	return redirect('events:service_detail', slug = event.slug, service_id = event.id)
# Create your views here.
