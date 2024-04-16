from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_home, name='main_home'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.user_login, name='login'),
    path('user_home/', views.user_home, name='user_home'),
    path('product_list/', views.product_list, name='product_list'),
    path('add_product/', views.add_product, name='add_product'),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-wishlist/<int:wishlist_item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('search/', views.search_products, name='search_products'),
    path('change_password/', views.change_password, name='change_password'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('logoutpage/', views.logoutpage, name='logoutpage'),
    path('create_category/', views.create_category, name='create_category'),
    path('list_categories/', views.list_categories, name='list_categories'),
    path('delete_category/', views.delete_category, name='delete_category'),
    path('update_category/', views.update_category, name='update_category'),
]
























# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.main_home, name='main_home'),
#     path('user/', views.user_home, name='user_home'),
#     path('dealer/', views.dealer_home, name='dealer_home'),
#     path('registration/', views.registration, name='registration'),
#     path('login/', views.login, name='login'),
# ]