from rest_framework import serializers
from .models import User, Task
from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email','full_name']

# Task Serializer
class TaskSerializer(serializers.ModelSerializer):
    #user = UserSerializer()

    class Meta:
        model = Task
        fields = [
            'id', 'user', 'date', 'task_type', 'priority', 'estimated_time',
            'actual_time_taken', 'task_description', 'task_status',
            'branch_name', 'pr_link', 'completion_date'
        ]
        # fields ='__all__'
