

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user.homr', views.user_home, name='user_home'),
    path('dealer.home', views.dealer_home, name='dealer_home'),
    path('user_register/', views.user_registration, name='user_registration'),
    path('dealer_register/', views.dealer_registration, name='dealer_registration'),
    path('login/', views.login, name='login'),
]
