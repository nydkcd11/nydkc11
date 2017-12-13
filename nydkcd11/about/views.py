#views seciton for about
#essetnially controllers for pages -- views put together all the necesary datapoints and pushes it to the templates
from django.shortcuts import render
from django.http import HttpResponse
from .models import Division, School, FAQ #models have to be imported
def division(request):
	member_list = Division.objects.order_by('-pk').reverse()
	return render(request, 'about/division.html',{'member_list':member_list,})
def clubs(request):
	school_list = School.objects.order_by('-pk').reverse()
	return render(request, 'about/school.html',{'school_list':school_list})
def faq(request):
	faq_list = FAQ.objects.order_by('-pk').reverse()
	return render(request, 'about/faq.html',{'faq_list':faq_list})
def index(request):
	return render(request, 'about/about.html')
# Create your views here.
