from django.shortcuts import render
from django.http import HttpResponse
from .models import DTC
def index(request):
	return HttpResponse("This is the events root page")
def dtc(request):
	dtc = DTC.objects.get(pk=1)
	return render(request, 'events/events.html',{'dtc':dtc})
# Create your views here.
