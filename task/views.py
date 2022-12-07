from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
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
    return render(request,'task/list.html',{'tasks':tasks,'form':form,'user':user})

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
