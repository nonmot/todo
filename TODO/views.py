from django.shortcuts import render
from .models import TodoList, Task
from .forms import TodoListForm, TaskForm
from django.shortcuts import redirect

# Create your views here.

def home(request):
    todolist = TodoList.objects.all()
    params = {
        'todolist': todolist,
    }
    return render(request, 'TODO/todolist.html', params)

def task(request, pk):
    tasks = Task.objects.filter(todolist__id = pk)
    todolist = TodoList.objects.get(id=pk)

    params = {
        'tasks': tasks,
        'todolist': todolist,
    }
    return render(request, 'TODO/task.html', params)

def newList(request):
    if request.method == 'POST':
        obj = TodoList()
        obj.owner = request.user
        newlist = TodoListForm(request.POST, instance=obj)
        newlist.save()
        return redirect(to='/')
    else:
        form = TodoListForm()
    params = {
        'form': form,
    }
    return render(request, 'TODO/newList.html', params)

def newTask(request, pk):
    if request.method == 'POST':
        obj = Task()
        obj.owner = request.user
        # Taskインスタンスのtodolistに現在のtodolistを設定
        obj.todolist = TodoList.objects.get(id=pk)
        newtask = TaskForm(request.POST, instance=obj)
        newtask.save()
        return redirect(to='/')
    else:
        form = TaskForm()
    params = {
        'form': form,
    }
    return render(request, 'TODO/newtask.html', params)