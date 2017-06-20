from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404
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
'''
def results(request,person_id):
	person = get_object_or_404(Person, pk = person_id)
	return render(request,'board/detail.html',{'person':person})	
'''
'''
def results(request, person_id): #temp, some kind of 404 thing going?
	try:
		obj = Person.objects.get(id=person_id)
		output = ""
		output += obj.name + "\n" + obj.school + "\n" + obj.desc
		return HttpResponse(output)
	except Person.DoesNotExist:
		raise Http404("Not found")
	return render(request,"board/detail.html",{'person':person})

def details(request, person_id):
	try:
		person = Person.objects.get(pk=question_id)
	except Person.DoesNotExist:
		raise Http404("The person you queried isn't part of the board.")
	return render(request,"board/detail.html",{'person':person})
'''

