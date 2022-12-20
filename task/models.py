# imported User from the auth User model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
class:
Task model is the main model when creating task objects
the fields are as follows:
user - foregin key to the imported User model, when that user is deleted the entire task is deleted
title - charfield to assign a name to new task objects 
complete - booleanField which default too false 
created  - the exact day/time when the task object was created

function: 
__str__ - too show easily readable oject names 
"""
class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    