from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PostForm, EmailForm
def index(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.author = request.user
			post.save()
			return redirect('contact:done')	
	else:
		form = PostForm()
	return render(request,'contact/contact.html',{'form':form})
def done(request):
	return render(request,'contact/thanks.html')
def email_process(request):
	if request.method == "POST":
			email_form = EmailForm(request.POST)
			if email_form.is_valid():
				email = email_form.save(commit=False)
				email.save()
	else:
		email_form = EmailForm()
	return redirect('contact:done')
# Create your views here.
