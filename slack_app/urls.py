from django.contrib import admin
from django.urls import path
from slack_app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    
    path('addpeople/',addpeople,name='addpeople'),
]