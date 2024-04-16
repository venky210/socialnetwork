from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .forms import RegistrationForm, ProductForm, WishlistForm,profileform,CategoryForm
from .models import User, Product, Wishlist,Category

 


def main_home(request):
    return render(request, 'main_home.html')

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.role = User.Role.DEALER if form.cleaned_data['is_dealer'] else User.Role.USERS
            user.save()
            login(request, user)
            if user.role == User.Role.DEALER:
                return redirect('add_product')
            else:
                return redirect('user_home')
    else:
        form = RegistrationForm()
    
    return render(request, 'registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.role == User.Role.DEALER:
                    return redirect('add_product')
                elif user.dealer_details == 'Category Management User':

                    return redirect('create_category')
                else:
                    return redirect('user_home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def user_home(request):
    products = Product.objects.all()
    return render(request, 'user_home.html', {'products': products})


def product_list(request):
    products = Product.objects.filter(dealer=request.user)
    return render(request, 'product_list.html', {'products': products})

def search_products(request):
    query = request.GET.get('query')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'search_results.html', {'products': products, 'query': query})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.dealer = request.user
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def update_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id, dealer=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'form': form})


def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id, dealer=request.user)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'delete_product.html', {'product': product})




def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})


def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    existing_wishlist_item = Wishlist.objects.filter(user=request.user, product=product).first()

    if existing_wishlist_item:
        messages.info(request, 'This item is already in your wishlist.')
        return redirect('wishlist')

    if request.method == 'POST':
        form = WishlistForm(request.POST)
        if form.is_valid():
            wishlist_item = form.save(commit=False)
            wishlist_item.user = request.user
            wishlist_item.product = product
            wishlist_item.save()
            messages.success(request, 'Item added to wishlist successfully.')
            return redirect('wishlist')
    else:
        form = WishlistForm()

    return render(request, 'add_to_wishlist.html', {'form': form, 'product': product})



def remove_from_wishlist(request, wishlist_item_id):
    wishlist_item = get_object_or_404(Wishlist, pk=wishlist_item_id, user=request.user)

    if request.method == 'POST':
        wishlist_item.delete()
        messages.success(request, 'Item removed from wishlist successfully.')
        return redirect('wishlist')

    return redirect('wishlist') 


def logoutpage(request):
    logout(request)
    return render(request,'main_home.html')


def change_password(request):
    if request.method=='POST':
        pw=request.POST['pw']
        username=request.session.get('username')
        UO=User.objects.get(username=username)
        UO.set_password(pw)
        UO.save()
        return HttpResponse('Password changed Successfully')
    return render(request,'change_password.html')

def profile_edit(request):
    form=profileform()
    user=request.user
    if request.method=='POST':
        form=profileform(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Profile Edit Successfully....</h1>')

    return render(request,'profile_edit.html',{'form':form})



def list_categories(request):
    categories = Category.objects.all()
    return render(request, 'list_categories.html', {'categories': categories})


def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('some-success-url')  # Redirect to a success page
    else:
        form = CategoryForm()
    return render(request, 'create_category.html', {'form': form})




def delete_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('some-success-url')  # Redirect to a success page
    return render(request, 'delete_category.html', {'category': category})

def update_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('some-success-url')  # Redirect to a success page
    return render(request, 'update_category.html', {'form': form, 'category': category})


