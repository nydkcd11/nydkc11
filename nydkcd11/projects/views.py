import random
from .colorgen import hexgen, rgbagen
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Level
def detail(request, level_id,slug):
	project = get_object_or_404(Level, pk=level_id)
	cover_color = rgbagen()
	box_1 = hexgen()
	box_2 = hexgen()
	box_3 = hexgen()
	if project.slug != slug:
		return redirect('projects:detail', slug=project.slug, level_id = project.id)
	return render(request, 'projects/projects.html',{'project':project,'cover_color':cover_color,'box_1':box_1,'box_2':box_2, 'box_3': box_3})
def detail_redirect(request, level_id):
	project = get_object_or_404(Level, pk = level_id)
	return redirect('projects:detail', slug = project.slug, level_id = project.id)
# Create your views here.
