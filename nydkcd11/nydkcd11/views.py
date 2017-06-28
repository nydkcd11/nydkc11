from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Image, Post, Article
def index(request):
	image_list = Image.objects.order_by('-post')[:6] #need way to sort by pub_date from post
	length = []
	for i in range(len(image_list)):
		length.append(i)
	blog_list = Post.objects.order_by('pub_date').reverse()[:4]
	article_list = Article.objects.all().reverse()[len(Article.objects.all())-4:]
	return render(request, 'nydkcd11/home.html',{'image_list':image_list,'length':length, 'blog_list':blog_list,'article_list':article_list})
