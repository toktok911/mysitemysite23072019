from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages 

def homepage(request):
	return render(request = request, 
				   template_name = 'main/home.html' , 
				   context = {"tutorials": Tutorial.objects.all})

def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST) # mapping the submitted form to the UserCreationForm
		if form.is_valid():
			user = form.save() #If the form is valid, then we just save this new User object (which is part of the form, so we save the form)
			# we can log in the user using the following two lines:
			username = form.cleaned_data.get('username')
			messages.success(request, "New account created: {username}")
			login(request,user)
			return redirect("main:homepage") # sending registered users to the homepage
		"""
		else: # handling invalid form input
			for x in form.error_messages: 
				#print(form.error_messages[x])
				#messages.error(request, f"{x}:{form.error_messages{x}}")
 
			return render(request = request, 
				  template_name = "main/register.html",
				  context = {"form": form}) """

	form = UserCreationForm
	return render(request = request, 
				  template_name = "main/register.html",
				  context = {"form": form})

"""
We don't need to pass messages through the context, 
though that's exactly what we'd do if there wasn't 
something already in place like Django's messaging! 
"""