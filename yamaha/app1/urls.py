from django.urls import path
from .views import home, user_home, dealer_home, user_registration, dealer_registration, login#product_home
#from .import views
urlpatterns = [
    path('', home, name='home'),
    path('user_home/', user_home, name='user_home'),
    path('dealer_home/', dealer_home, name='dealer_home'),
    path('user_registration/', user_registration, name='user_registration'),
    path('dealer_registration/', dealer_registration, name='dealer_registration'),
    path('login/', login, name='login'),
    #path('product_home/',product_home, name='product_home')
]
