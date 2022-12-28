"""
imported packages:
redirect from shortcuts - forward the use back to the root list view 
login_required from auth.decorators - only authenticated users can see certain features
Task - Imported Task from models 
Imported both TaskForm and UserRegistrationForm from forms
"""
from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
"""
    :Function name - todo_list
 
    :variables 
        - user: gets the currently logged in user 
        - tasks: queryset that filters all the Task objects for that loggged in user 
 
    :Function Description 
        - gets all the users tasks, returns a post respond if the user creates a task else 
          returns a get respond for the user to create that task 

"""
@login_required
def todo_list(request):
    user = request.user
    tasks = Task.objects.filter(user=user)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            task = Task.objects.create(title=cd['title'],user=user)
            task.save()
        return redirect('/')
    else:
        form = TaskForm()
    context = {
        'tasks':tasks,
        'form':form,
        'user':user
    }
    return render(request,'task/list.html',context)

"""
    :Function name - update_task 
 
    :variables 
        - task: queryset that gets a task based on the url id
 
    :Function Description 
        - gets a task based on the id and creates a new taskform object with the instance
          of that task. if the user submits a post request the function creates a new tasklform 
          object with the user submitted infromation and save the new taskform object. 
"""
@login_required
def update_task(request,id):
    task = Task.objects.get(id=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context= {
        'form':form
    }
    return render(request,'task/update_task.html',context)

"""
    :Function name - delete_task 
 
    :variables 
        - task: queryset that gets a task based on the url id
 
    :Function Description 
        - gets a task based on the id and if the user submits a post request that task is deleted,
          then redirects the user back to the home page. 
"""
@login_required
def delete_task(request,id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    context = {
        'task':task
    }
    return render(request,'task/delete.html',context)

"""
    :Function name - register
 
    :variables 
        - task: queryset that gets a task based on the url id
 
    :Function Description 
        - if the user submits a post request a new UserRegistrationForm object is created.
          checks if all the user information is_valid and creates that new user. 
"""
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
        # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
        # Set the chosen password
            new_user.set_password(
            user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,'task/register_done.html',{'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        return render(request,'task/register.html',{'user_form': user_form})
