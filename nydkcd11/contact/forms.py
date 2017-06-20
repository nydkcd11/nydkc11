from django import forms
from .models import Contact

class PostForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ('name','school','email','title','text')
