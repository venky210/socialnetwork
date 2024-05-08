from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from app.forms import UserLoginForm,CategoryForm
from .models import Category

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or somewhere else
                return redirect('create_category')
            else:
                # Authentication failed
                error_message = "Invalid username or password."
    else:
        form = UserLoginForm()
        error_message = None

    return render(request, 'login.html', {'form': form, 'error_message': error_message})


from django.shortcuts import render, redirect
from .forms import CategoryForm
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form instance to the database
            return redirect('view_categories')  # Redirect to view_categories URL upon successful form submission
    else:
        form = CategoryForm()
    
    return render(request, 'create_category.html', {'form': form})





def view_categories(request):
    categories = Category.objects.all()
    return render(request, 'view_categories.html', {'categories': categories})


