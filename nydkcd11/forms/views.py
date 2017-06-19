from django.shortcuts import render
from django.http import HttpResponse
from .models import Papers
from blog.models import Link
def index(request):
	return HttpResponse("this is the forms page")
def papers(request):
	papers_list = Papers.objects.all()
	return render(request,'forms/papers.html',{'papers_list':papers_list})
def signup(request):
	return HttpResponse("this is the official signup page")
# Create your views here.
