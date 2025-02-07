from django.urls import path
from .views import *
#TaskListCreateView, 
#TaskDetailView, UserListView, UserDetailView

urlpatterns = [
    path('post-category/',post_category),
    path('post-product/',post_product),
    path('get-category/',get_category),
    path('get-product/',get_product),

    
    # path('get-task/<int:user_id>',get_task_by_id),
    # path('update-task/',update_task),

    ]