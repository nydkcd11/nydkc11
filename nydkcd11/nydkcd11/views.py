from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Image
def index(request):
	image_list = Image.objects.all() #need way to sort by pub_date from post
	length = []
	for i in range(len(image_list)):
		length.append(i)
	print(length)
	return render(request, 'nydkcd11/home.html',{'image_list':image_list,'length':length})
