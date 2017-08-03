from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Post, Article
from blog.page import page 
# Create your views here.
def index(request):
	latest_post_list = Post.objects.order_by('-pub_date_2')
	posts = page(latest_post_list,request)
	return render(request, 'blog/index.html',{'posts':posts})
def article(request):
	articles_query = Article.objects.order_by('-pk')
	articles = page(articles_query,request)	
	return render(request, 'blog/newslist.html',{'articles':articles})
def detail(request, post_id, slug):
	'''
	try:
		post = Post.objects.get(pk=post_id)
	except Post.DoesNotExist:
		raise Http404("Post doesn't exist")
	return render(request, 'blog/detail.html',{'post' : post})
	'''
	post = get_object_or_404(Post, pk = post_id)
	image_list = post.image_set.all()
	if post.slug != slug:
		return redirect('blog:detail', slug = post.slug, post_id = post.id)
	return render(request, 'blog/detail.html',{'post':post,'image_list':image_list}) #note: set to extending service
def detail_redirect(request, post_id):
	post = get_object_or_404(Post, pk = post_id)
	return redirect('blog:detail', slug = post.slug, post_id = post.id)
def news(request, article_id, slug):
	article = get_object_or_404(Article, pk = article_id)
	if article.slug != slug:
		return redirect('blog:news', slug = article.slug, article_id = article.id)
	return render(request, 'blog/article.html',{'article':article})
def news_redirect(request, article_id):
	article = get_object_or_404(Article, pk = article_id)
	return redirect('blog:news', slug = article.slug, article_id = article.id)
