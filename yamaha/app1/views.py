from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, DealerRegistrationForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def user_home(request):
    return render(request, 'user_home.html')

def dealer_home(request):
    return render(request, 'dealer_home.html')

def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_home.html') 
    else:
        form = UserRegistrationForm()
    return render(request, 'user_registration.html', {'form': form})

def dealer_registration(request):
    if request.method == 'POST':
        form = DealerRegistrationForm(request.POST)
        if form.is_valid():
             form.save()
             return redirect('dealer_home')
    else:
        form = DealerRegistrationForm()
    return render(request, 'dealer_registration.html', {'form': form})


from django.contrib.auth import authenticate, login as auth_login

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
           # auth_login(request, user) 
           if user :
            return redirect('dealer_home') 
        else:
            return redirect('user_home') 
    else:
        return render(request, 'login.html')

# def product_home(request):
#     if request.method == 'POST':
#         form =  ProductForm(request.POST)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.dealer  = request.user
#             product.save()
#             return redirect('product_list')
#     else:
#         form = ProductForm()
#     return render(request, 'create_product.html', {'form': form})


