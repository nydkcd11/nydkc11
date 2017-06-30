from django import forms
from .models import Contact, Email

class PostForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ('name','school','email','title','message')
class EmailForm(forms.ModelForm):
	class Meta:
		model = Email
		fields = ('email',)
