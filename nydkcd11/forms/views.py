from django.shortcuts import render
from django.http import HttpResponse
from .models import Papers
from blog.models import Link
def index(request):
	return HttpResponse("this is the forms page")
def papers(request):
	return HttpResponse("this is the official paperwork page")
def signup(request):
	return HttpResponse("this is the official signup page")
# Create your views here.
