from django.db import models
from django.utils import timezone
from account.models import CustomUser

# Create your models here.
class TodoList(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='todolist_owner')
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=10, choices=(
        ('#FFBEDA', 'red'),
        ('#FFC7AF', 'orange'),
        ('#FFFF88', 'yellow'),
        ('#FF77FF', 'pink'),
        ('#DCC2FF', 'purple'),
        ('#B1F9D0', 'green'),
        ('#BAD3FF', 'blue'),
    ), default='blue')

class Task(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='task_owner')
    todolist = models.ForeignKey('Todolist', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    note = models.TextField(max_length=100)
    deadline = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    priority = models.BooleanField()