from django.shortcuts import render
from django.http import HttpResponse
from .models import Division, School, FAQ
def index(request):
	return HttpResponse("this is the new about page")
def division(request):
	member_list = Division.objects.all()
	test = []
	for i in range(len(member_list)):
		test.append(i)
	print(test)
	count=0
	return render(request, 'about/division.html',{'member_list':member_list,'count':count})
def clubs(request):
	school_list = School.objects.all()
	return render(request, 'about/school.html',{'school_list':school_list})
def faq(request):
	faq_list = FAQ.objects.all()
	return render(request, 'about/faq.html',{'faq_list':faq_list})
# Create your views here.
