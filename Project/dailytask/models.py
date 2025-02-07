from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)  
    full_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.full_name


class Task(models.Model):
    TYPE_CHOICES=[
        ('Task','Task'),
        ('Bug','Bug'),
    ]
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    ]

    STATUS_CHOICES = [
        ('To-Do','To-Do'),
        ('Commited', 'Commited'),
        ('In-Progress', 'InProgress'),
        ('Completed', 'Completed'),
        ('Defer', 'Defer'),
    ]
    
  
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,null=True,related_name="tasks")
    date = models.DateField(auto_now_add=True)
    task_type = models.CharField(max_length=255,choices=TYPE_CHOICES,blank=True,null=True,default='Task')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES,blank=True,null=True,default='Low ')
    estimated_time = models.CharField(max_length=255,help_text="Estimated time in hours",blank=True,null=True,)
    actual_time_taken = models.CharField(max_length=255,help_text="Actual time taken in hours", null=True, blank=True)
    task_description = models.TextField(blank=True,null=True)
    task_status = models.CharField(max_length=15, choices=STATUS_CHOICES,blank=True,null=True,default='To-Do')
    branch_name = models.CharField(max_length=100, null=True, blank=True)
    pr_link = models.CharField(max_length=255, null=True, blank=True)
    completion_date = models.DateField(auto_now=True,null=True, blank=True)

    # def __str__(self):
    #     return self.task_status
 
