from django.urls import path
from app.views import *
urlpatterns = [
    path('',home,name='home'),
    path('registration/',registration,name='registration'),
    # path('user_login/',user_login,name='user_login'),
    
]