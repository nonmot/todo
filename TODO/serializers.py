from rest_framework import serializers
from .models import TodoList, Task
from account.models import CustomUser

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username']

class TodoListSerialzer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodoList
        fields = ['owner', 'title', 'color']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['owner', 'todolist', 'title', 'note', 'deadline', 'created_date', 'priority']