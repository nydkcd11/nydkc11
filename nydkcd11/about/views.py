from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	return HttpResponse("this is the new about page")
# Create your views here.
