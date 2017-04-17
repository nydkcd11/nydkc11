from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django.template import loader
# Create your views here.
def index(request):
	names_list = Person.objects.all()
	template = loader.get_template('board/index.html')
	context = {
		'names_list' : names_list	
	}
	#return HttpResponse(template.render(context, request))
	return render(request, 'board/index.html', context)
def results(request, person_id): #temp
	obj = Person.objects.get(id=person_id)
	output = ""
	output += obj.name + "\n" + obj.school + "\n" + obj.desc
	return HttpResponse(output)
