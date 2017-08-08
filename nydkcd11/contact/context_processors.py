from .forms import EmailForm
import random
def email_form(request):
	return{'email_form':EmailForm()}
def number(request):
	return{'number':random.randint(1,101)}
