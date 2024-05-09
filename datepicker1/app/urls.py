from app.views import *
from django.urls import path

urlpatterns = [
        path('datepicker/', datepicker_view, name='datepicker'),
        path('date_display/', date_display, name='date_display'),
        path('create_time/', create_selected_time, name='create_selected_time'),
        path('time_list/', selected_time_list, name='selected_time_list'),

]