from app.views import *
from django.urls import path

urlpatterns = [
        path('datepicker/', datepicker, name='datepicker'),
        path('date_display/', date_display, name='date_display'),
        path('',homepage,name='homepage'),
        path('registration/',registration,name='registration'),
        path('user_login/',user_login,name='user_login'),
        path('add_task/',add_task,name='add_task'),
        path('view_tasklist/',view_tasklist,name='view_tasklist'),
        path('search/', search_tasks, name='search_tasks'),
        path('logout/', logout, name='logout'),
        path('update_task/<int:task_id>/', update_task, name='update_task'),
        path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
        path('pending_tasks/', pending_tasks, name='pending_tasks'),
        path('completed_tasks/',completed_tasks, name='completed_tasks'),

]