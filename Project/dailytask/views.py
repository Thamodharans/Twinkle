from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password

# User Views
@api_view(['POST'])
def post_user(request):
    variable1=UserSerializer(data=request.data)
    if variable1.is_valid():
        variable1.save()
        return Response({'message': 'User created successfully', 'user': variable1.data}, status=status.HTTP_201_CREATED)
    return Response(variable1.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_user(request):
   variable2=User.objects.all()
   serializers=UserSerializer(variable2,many=True)
   return Response(serializers.data, status=status.HTTP_200_OK )
   #return Response(serializers.data,status=status.HTTP_200_OK)


@api_view(['POST'])
def post_task(request):
    task=TaskSerializer(data=request.data)
    if task.is_valid():
        task.save()
        return Response({'message': 'Task created successfully', 'task': task.data}, status=status.HTTP_201_CREATED)
    return Response(task.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_task(request):
   task=Task.objects.all()
   serializers=TaskSerializer(task,many=True)
   return Response(serializers.data, status=status.HTTP_200_OK )
   #return Response(serializers.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_task_by_id(request, user_id):
    try:
        tasks = Task.objects.filter(user__id=user_id)  # Use user__id if 'user' is a ForeignKey
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

@api_view(['PUT'])
def update_task(request):
    """
    Update task details using user_id and task_id as query parameters.
    If the PR link is updated, the task status will be set to "Committed".
    """
    # Extract user_id and task_id from query parameters
    user_id = request.query_params.get('user_id')
    task_id = request.query_params.get('task_id')

    # Validate that user_id and task_id are provided
    if not user_id or not task_id:
        return Response({'error': 'user_id and task_id are required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Fetch the task based on both user_id and task_id
        task = Task.objects.get(user_id=user_id, id=task_id)
    except Task.DoesNotExist:
        # Return error if task with given user_id and task_id does not exist
        return Response({'error': 'Task not found for the given user and task ID'}, status=status.HTTP_404_NOT_FOUND)

    # Check if the PR link is provided in the request data
    if 'pr_link' in request.data:
        # If PR link is updated, set task status to 'Committed'
        task.status = 'Committed'

    # Serialize the task with the incoming data and allow partial updates
    serializer = TaskSerializer(task, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Task updated successfully", "task": serializer.data}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  