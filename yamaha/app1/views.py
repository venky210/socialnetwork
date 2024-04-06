from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, DealerRegistrationForm
from django.contrib.auth import authenticate,login#ProductForm
from django.http import HttpResponse
from .models import User
from django.contrib import auth

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
          # form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']
            user = User.objects.create(username=username)
            user.set_password(password)
            return redirect('user_home') 
    else:
        form = UserRegistrationForm()
    return render(request, 'user_registration.html', {'form': form})

def dealer_registration(request):
    if request.method == 'POST':
        form = DealerRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']
            user = User.objects.create(username=username,email=email)
            user.set_password(password)
            auth.login(request,user)
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


# def product_list(request):
#     products = Products.objects.filter(dealer=request.user)
#     return render(request, 'product_list.html', {'products': products})

  
# def add_product(request):
#     if request.method == 'POST':
#         form = ProdutForm(request.POST)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.dealer = request.user
#             product.save()
#             return redirect('product_list')
#     else:
#         form = ProdutForm()
#     return render(request, 'ProductForm.html', {'form': form})


