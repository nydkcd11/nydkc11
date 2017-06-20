from django.shortcuts import render
from django.http import HttpResponse
from .models import Division, School
def index(request):
	return HttpResponse("this is the new about page")
def division(request):
	member_list = Division.objects.all()
	return render(request, 'about/division.html',{'member_list':member_list})
	return HttpResponse("this is the divison page")
def clubs(request):
	school_list = School.objects.all()
	return render(request, 'about/school.html',{'school_list':school_list})
# Create your views here.
