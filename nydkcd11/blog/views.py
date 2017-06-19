from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Post
# Create your views here.
def index(request):
	#latest_post_list = Post.objects.order_by('-pub_date')[:5]
	latest_post_list = Post.objects.all()
	template = loader.get_template('blog/index.html')
	context = {
		'latest_post_list': latest_post_list,	
	}
	#return HttpResponse(template.render(context,request))
	return render(request, 'blog/index.html',context)
def detail(request, post_id):
	'''
	try:
		post = Post.objects.get(pk=post_id)
	except Post.DoesNotExist:
		raise Http404("Post doesn't exist")
	return render(request, 'blog/detail.html',{'post' : post})
	'''
	post = get_object_or_404(Post, pk = post_id)
	return render(request, 'blog/detail.html',{'post':post})
