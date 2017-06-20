from django.shortcuts import render
from django.http import HttpResponse
from .models import Papers
from blog.models import Link
def papers(request):
	papers_list = Papers.objects.all()
	return render(request,'forms/papers.html',{'papers_list':papers_list})
def signup(request):
	link_list = Link.objects.all()
	return render(request, 'forms/signup.html',{'link_list':link_list})
	return HttpResponse("this is the official signup page")
# Create your views here.
