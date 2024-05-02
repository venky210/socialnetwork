from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from app.forms import *
from django.contrib.auth import authenticate,login

# Create your views here.


def homepage(request):
    return render(request,'homepage.html')

def registration(request):
    UFO=userform()

    d={'user':UFO}
    if request.method=='POST':
        ufd=userform(request.POST)
       
        if ufd.is_valid():
            MUFDO=ufd.save(commit=False)
            pw=ufd.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()
            
            return HttpResponse('Registration is successfully')
        else:
            return HttpResponse('user already register...')
    return render(request,'registration.html',d)



def user_login(request):
    if request.method=='POST':
        un=request.POST['un']
        pw=request.POST['pw']
        AUO=authenticate(username=un,password=pw)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=un
            return HttpResponse('login success')
        else:
            return HttpResponse('Provide Vaild User And Password...')
        
    return render (request,'loginpage.html')


def todolist(request):
    form=todolistform()
    if request.method=='POST':
        form=todolistform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('task register successfully')
    return render(request,'todolist.html',{'form':form})