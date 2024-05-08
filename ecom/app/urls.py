from app.views import *
from django.urls import path

urlpatterns = [
        path('login/', user_login, name='user_login'),
        path('create_category/', create_category, name='create_category'),
        path('category_list/',category_list, name='category_list'),





]