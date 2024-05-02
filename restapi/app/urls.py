from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('add_product/', add_product, name='add_product'),
    path('product_list/', product_list, name='product_list'),
    path('update_product/<int:pk>/',update_product, name='update_product'),
    path('delete_product/<int:pk>/', delete_product, name='delete_product'),
    path('add_to_wishlist/<int:pk>/', add_to_wishlist, name='add_to_wishlist'),
    path('user_product_list/',user_product_list, name='user_product_list'),
   








    
    
]