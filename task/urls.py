from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
"""
Created url paths for corresponding view functions 
"""

app_name = 'Task'

urlpatterns = [
    path('',views.todo_list,name='list'),
    path('update_task/<int:id>/',views.update_task, name='update'),
    path('delete/<int:id>/',views.delete_task,name='delete'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
