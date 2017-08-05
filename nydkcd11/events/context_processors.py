from .models import Convention
def conventions(request):
	conventions = Convention.objects.all()
	return {'conventions':conventions}
