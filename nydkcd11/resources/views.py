from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Video, Image
from .models import Newsletter, Minutes
from blog.page import page
def videos(request):
	video_list = page(Video.objects.order_by('-post'),request)
	context = {
		'video_list':video_list,	
	}
	return render(request,'resources/videos.html',context)
def minutes(request):
	minutes_list = Minutes.objects.order_by('-pk').reverse()
	return render(request,'resources/minutes.html',{'minutes_list':minutes_list})
def month_parse(num):
	month_dict = {
		1:'January',
		2:'February',
		3:'March',
		4:'April',	
		5:'May',	
		6:'June',	
		7:'July',	
		8:'August',	
		9:'September',	
		10:'October',	
		11:'November',	
		12:'December',	
	}
	return month_dict[int(num)]
def month_gen(year):
	month_groups = {}
	for i in range(1,12):
		if Image.objects.filter(post__pub_date_2__year=year).filter(post__pub_date_2__month = i).exists():
			month_groups[i]=i
	return month_groups
def gallery_dict(): #equivalent of calling .objects.all() ish
	images = Image.objects.order_by('-post')
	images_grouped = {}
	for image in images:
		try:
			images_grouped[image.post.pub_date_2.year]
		except KeyError:
			images_grouped[image.post.pub_date_2.year] = month_gen(image.post.pub_date_2.year)	
	return images_grouped
def sitemap_dict():
	thing = gallery_dict()
	output = []
	for year,months in thing.items():
		for month in months:
			output.append({'year':year,'month':month})
	return output
def gallery(request):
	images_grouped = gallery_dict()
	return render(request,'resources/gallery.html',{'images_grouped':images_grouped})
def gallery_specific(request, year, month):
	images = Image.objects.filter(post__pub_date_2__year = year).filter(post__pub_date_2__month = month)
	if len(images) == 0:
		return redirect('resources:gallery')
	return render(request, 'resources/gallery_specific.html', {'images':images, 'year':year,'month':month_parse(month)})
# Create your views here.
