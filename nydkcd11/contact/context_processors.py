from .forms import EmailForm

def email_form(request):
	return{'email_form':EmailForm()}
