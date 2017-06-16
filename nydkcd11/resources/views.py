from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	return HttpResponse("hello you are at response")
# Create your views here.
