# imported views from project directory, views as auth_views from auth 
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'Task'


"""
Project urls:
list - root view which shows the list of created task, and the form too create new task 
register - user creation url
update - User update operation
delete - user delete operation 
login - class based user login 
logout - class based user logout 
"""
urlpatterns = [
    path('',views.todo_list,name='list'),
    path('update_task/<int:id>/',views.update_task, name='update'),
    path('delete/<int:id>/',views.delete_task,name='delete'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
