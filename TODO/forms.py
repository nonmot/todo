from django import forms
from .models import TodoList, Task
from django.contrib.auth.models import User

#TodoListのフォーム
class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['title', 'color']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.Select(attrs={'class': 'form-control'})
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'note', 'deadline', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control'}),
            'deadline': forms.SelectDateWidget(attrs={'class': 'form-control'}),
        }