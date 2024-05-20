
from django.urls import path
from app.views import *

urlpatterns = [
    path('',view_profile,name='view_profile')
]