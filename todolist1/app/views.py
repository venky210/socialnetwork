from django.shortcuts import render,HttpResponse,redirect
from app.forms import *
from app.models import *
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
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        AUO = authenticate(username=un, password=pw)
        if AUO and AUO.is_active:
            login(request, AUO)
            request.session['username'] = un
            return redirect('add_task')  # Assuming 'todolist' is the name of the URL pattern for todolist.html
        else:
            return HttpResponse('Provide Valid User And Password...')
        
    return render(request, 'loginpage.html')



def add_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_tasklist')  # Redirect to the 'todolist' view
    return render(request, 'add_task.html', {'form': form})



def view_tasklist(request):
    tasks = Task.objects.all()
    return render(request, 'view_tasklist.html', {'tasks': tasks})

def search_tasks(request):
    query = request.GET.get('query')
    if query:
        tasks = Task.objects.filter(name__icontains=query)
    else:
        tasks = Task.objects.all()
    return render(request, 'search_results.html', {'tasks': tasks, 'query': query})

