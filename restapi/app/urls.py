from django.urls import path
from app.views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('add_product/',add_product,name='add_product'),
    path('product_list/',product_list,name='product_list'),
    path('update_product/<int:pk>/', update_product, name='update-product'),
    path('delete_product/<int:pk>/', delete_product, name='delete-product'),

    path('add_to_wishlist/<int:product_id>/', add_product_to_wishlist, name='add_product_to_wishlist'),
    path('view_wishlist/', view_wishlist, name='view_wishlist'),
    path('remove_from_wishlist/<int:wishlist_item_id>/', remove_from_wishlist, name='remove_from_wishlist'),
    path('add_to_cart/<int:product_id>/', add_product_to_cart, name='add_to_cart'),
    path('cart_list/', cart_list, name='cart_list'),
    path('remove_from_cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),






]