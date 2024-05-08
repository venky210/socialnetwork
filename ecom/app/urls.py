from app.views import *
from django.urls import path

urlpatterns = [
        path('login/', user_login, name='user_login'),
        path('create_category/', create_category, name='create_category'),
        path('view_categories/', view_categories, name='view_categories'),




]