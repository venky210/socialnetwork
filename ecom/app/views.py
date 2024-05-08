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





def create_category(request):
    if request.method == 'POST':  # If the request method is POST (form submission)
        form = CategoryForm(request.POST)  # Bind form data to CategoryForm
        if form.is_valid():  # If form data is valid
            category = form.save()  # Save the form data to create a new Category object
            return redirect('category_list')  # Redirect to the category list page
    else:
        form = CategoryForm()  # If the request method is GET, create a new, empty CategoryForm
    
    return render(request, 'create_category.html', {'form': form})  # Render the create_category.html template with the form






def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})




