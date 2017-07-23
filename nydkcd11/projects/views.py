import random
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Level
def detail(request, level_id,slug):
	project = get_object_or_404(Level, pk=level_id)
	colors = [
		'#231f20',
		'#003366',
		'#b49759',
		'#00aeef',
		'#f58025',
		'#91381e',
		'#c41230',
		'#ec008c',
		'#729849',
		'#fed450',
	]
	colors_2 = [
		'rgba(35,31,32, 0.3)',
		'rgba(0,47,95, 0.3)',
		'rgba(180,151,90, 0.3)',
		'rgba(0,174,239, 0.3)',
		'rgba(245,128,37, 0.3)',
		'rgba(145,56,31, 0.3)',
		'rgba(196,18,48, 0.3)',
		'rgba(236,0,140, 0.3)',
		'rgba(115,152,73, 0.3)',
		'rgba(255,210,79, 0.3)',
	]
	cover_color = colors_2[random.randint(0,len(colors_2)-1)]
	box_1 = colors[random.randint(0,len(colors)-1)]
	box_2 = colors[random.randint(0, len(colors)-1)]
	box_3 = colors[random.randint(0, len(colors)-1)]
	if project.slug != slug:
		return redirect('projects:detail', slug=project.slug, level_id = project.id)
	return render(request, 'projects/projects.html',{'project':project,'cover_color':cover_color,'box_1':box_1,'box_2':box_2, 'box_3': box_3})
def detail_redirect(request, level_id):
	project = get_object_or_404(Level, pk = level_id)
	return redirect('projects:detail', slug = project.slug, level_id = project.id)
# Create your views here.
