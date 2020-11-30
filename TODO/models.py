from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodoList(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todolist_owner')
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=10, choices=(
        ('red', 'red'),
        ('orange', 'orange'),
        ('yellow', 'yellow'),
        ('pink', 'pink'),
        ('purple', 'purple'),
        ('green', 'green'),
        ('blue', 'blue'),
    ), default='blue')

class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_owner')
    todolist = models.ForeignKey('Todolist', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    note = models.TextField(max_length=100)
    deadline = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    priority = models.BooleanField()