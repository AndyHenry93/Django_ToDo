# imported the Task model
from django.contrib import admin
from .models import Task

# Register your models here.
# Added the task model to the admin page to view the object title, completion status and creation date.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','complete','created_date')