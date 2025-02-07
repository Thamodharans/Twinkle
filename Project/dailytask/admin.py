from django.contrib import admin
from .models import User, Task

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ( 'email', 'full_name')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_type', 'priority', 'task_status', 'user', 'completion_date')
    #search_fields = ('task_type', 'priority', 'task_status', 'user__username')
