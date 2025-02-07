from django.urls import path
from .views import *
#TaskListCreateView, 
#TaskDetailView, UserListView, UserDetailView

urlpatterns = [
    path('post-users/',post_user),
    path('get-users/',get_user),
    path('get-task/',get_task),
    path('post-task/',post_task),
    path('get-task/<int:user_id>',get_task_by_id),
    path('update-task/',update_task),

    ]
