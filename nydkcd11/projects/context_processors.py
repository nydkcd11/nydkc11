from .models import Level
def projects(request):
	projects = Level.objects.all()
	return {'projects':projects}
