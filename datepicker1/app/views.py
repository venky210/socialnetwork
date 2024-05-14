
from django.shortcuts import render, redirect,HttpResponse,get_object_or_404
from app.forms import *
from app.models import *
from django.contrib.auth import authenticate,login,logout
from datetime import datetime  

def datepicker(request):
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form = DateForm()
    return render(request, 'datepicker_form.html', {'form': form})

def date_display(request):
    selected_date = SelectedDate.objects.last()  
    return render(request, 'view_tasklist', {'selected_date': selected_date})


def create_selected_time(request):
    if request.method == 'POST':
        form = SelectedTimeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('selected_time_list')  
    else:
        form = SelectedTimeForm()
    return render(request, 'selected_time_form.html', {'form': form})

def selected_time_list(request):
    selected_times = SelectedTime.objects.all()
    return render(request, 'selected_time_list.html', {'selected_times': selected_times})

 
def homepage(request):
    return render(request,'homepage.html')

def registration(request):
    form=userform()

    d={'user':form}
    if request.method=='POST':
        user=userform(request.POST)
       
        if user.is_valid():
            modifyuser=user.save(commit=False)
            pw=user.cleaned_data['password']
            modifyuser.set_password(pw)
            modifyuser.save()
            
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
            return redirect('datepicker')  # Assuming 'todolist' is the name of the URL pattern for todolist.html
        else:
            return HttpResponse('Provide Valid User And Password...')
        
    return render(request, 'loginpage.html')


def search_tasks(request):
    query = request.GET.get('query')
    if query:
        tasks = Task.objects.filter(title__icontains=query)   
    else:
        tasks = Task.objects.all()
    return render(request, 'search_results.html', {'tasks': tasks, 'query': query})


# def add_task(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             task = form.save(commit=False)
#             # Here, you can perform any additional operations before saving the task
#             task.save()
#             return redirect('view_tasklist')  # Redirect to the 'view_tasklist' view after saving
#     else:
#         form = TaskForm()
#     return render(request, 'add_task.html', {'form': form})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.time = datetime.strptime(request.POST['time'], '%H:%M').time()  
            task.save()
            return redirect('view_tasklist')  
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})





def view_tasklist(request):
    tasks = Task.objects.all()
    return render(request, 'view_tasklist.html', {'tasks': tasks})




def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('view_tasklist')  
    return render(request, 'update_task.html', {'form': form})

def pending_tasks(request):
    pending_tasks = Task.objects.filter(completed=False)
    return render(request, 'pending_tasks.html', {'pending_tasks': pending_tasks})


def completed_tasks(request):
    completed_tasks = Task.objects.filter(completed=True)
    return render(request, 'completed_tasks.html', {'completed_tasks': completed_tasks})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('view_tasklist')  # Redirect to the 'view_tasklist' view
    return render(request, 'delete_task.html', {'task': task})

def logout(request):
    return render(request,'homepage.html')

