from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Level
def index(request):
	return HttpResponse("response")
def detail(request, level_id):
	project = get_object_or_404(Level, pk=level_id)
	return HttpResponse("test")
# Create your views here.
