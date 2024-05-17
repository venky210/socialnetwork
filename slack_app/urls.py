from django.contrib import admin
from django.urls import path
from slack_app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',slack,name='slack'),
    path('editchannel/',editchannel,name='editchannel'),
    path('addpeople/',addpeople,name='addpeople'),
]