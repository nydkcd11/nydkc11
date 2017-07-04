from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Post, Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def index(request):
	#latest_post_list = Post.objects.order_by('-pub_date')[:5]
	latest_post_list = Post.objects.order_by('-pub_date')
	template = loader.get_template('blog/index.html')
	context = {
		'latest_post_list': latest_post_list,	
	}
	paginator = Paginator(latest_post_list,5)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator,num_pages)
	return render(request, 'blog/index.html',{'posts':posts})
def article(request):
	articles = Article.objects.order_by('-pk')
	paginator = Paginator(articles,5)
	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPagE:
		articles = paginator.page(paginator, num_pages)
	return render(request, 'blog/newslist.html',{'articles':articles})
def detail(request, post_id):
	'''
	try:
		post = Post.objects.get(pk=post_id)
	except Post.DoesNotExist:
		raise Http404("Post doesn't exist")
	return render(request, 'blog/detail.html',{'post' : post})
	'''
	post = get_object_or_404(Post, pk = post_id)
	image_list = post.image_set.all()
	return render(request, 'blog/detail.html',{'post':post,'image_list':image_list}) #note: set to extending service
def news(request, article_id):
	article = get_object_or_404(Article, pk = article_id)
	return render(request, 'blog/article.html',{'article':article})
