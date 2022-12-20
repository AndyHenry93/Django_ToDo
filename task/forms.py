# imported the Task model, and User model
from django import forms
from .models import Task
from django.contrib.auth.models import User

"""
TaskForm class is the main interaction with the user to create a new task
each form has one field 'title' where users input new task. 
The TaskForm is created based on the Task model and includes the fields title and complete
"""
class TaskForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    class Meta:
        model = Task
        fields = ('title','complete')

"""
class:
UserRegistrationForm class is the main form for create new user accounts.
the form uses the User model to capture the users desired username, firstname and email. 

function:
The form also asks the user for a password which they have too confirm.
once confirmed the clean_password function validated if the passwords arent the same 
and raises a form vallidation error, if they are it returns the valid password. 
"""
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
def clean_password2(self):
    cd = self.cleaned_data
    if cd['password'] != cd['password2']:
        raise forms.ValidationError('Passwords don\'t match.')
    else:
        return cd['password2']