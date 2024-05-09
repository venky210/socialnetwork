from app.views import *
from django.urls import path

urlpatterns = [
        path('', datepicker_view, name='datepicker'),
        path('display/', date_display, name='date_display'),

]