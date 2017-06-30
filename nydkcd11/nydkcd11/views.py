from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Image, Post, Article
from contact.forms import EmailForm
def index(request):
	image_list = Image.objects.order_by('-post')[:6] #need way to sort by pub_date from post
	length = []
	for i in range(len(image_list)):
		length.append(i)
	blog_list = Post.objects.order_by('pub_date').reverse()[:4]
	article_list = Article.objects.order_by('-pk').reverse()[:4]
	if request.method == "POST":
		form = EmailForm(request.POST)
		if form.is_valid():
			email = form.save(commit=False)
			email.save()
			return redirect('index')
	else:
		form = EmailForm()
	return render(request, 'nydkcd11/home.html',{'image_list':image_list,'length':length, 'blog_list':blog_list,'article_list':article_list, 'form':form,})
