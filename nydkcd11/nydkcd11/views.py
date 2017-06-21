from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Image, Post
def index(request):
	image_list = Image.objects.all() #need way to sort by pub_date from post
	length = []
	for i in range(len(image_list)):
		length.append(i)
	blog_list = Post.objects.order_by('pub_date').reverse()[:4]
	return render(request, 'nydkcd11/home.html',{'image_list':image_list,'length':length, 'blog_list':blog_list})
