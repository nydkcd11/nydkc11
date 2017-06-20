from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	return HttpResponse("this is the new about page")
def division(request):
	return HttpResponse("this is the divison page")
def clubs(request):
	return HttpResponse("this is the clubs page")
# Create your views here.
