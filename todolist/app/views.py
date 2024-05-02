
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect,HttpResponse
from .forms import RegistrationForm
from app.models import *


def home(request):
    return render(request, 'home.html')

def registration(request):
    if request.method == 'POST': 
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return HttpResponse('User Registration Successfull')
        return HttpResponse('invalid password username')
    else:
        form = RegistrationForm()
    
    return render(request, 'registration.html', {'form': form})