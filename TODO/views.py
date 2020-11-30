from django.shortcuts import render
from .models import TodoList, Task
from .forms import TodoListForm, TaskForm
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

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
        #リダイレクト先に元のTodolistに戻したい
        redirect_path = '/task/' + str(pk)
        return redirect(to=redirect_path)
    else:
        form = TaskForm()
    params = {
        'form': form,
        'id': pk,
    }
    return render(request, 'TODO/newtask.html', params)

def deleteTodolist(request, pk):
    if request.method == 'POST':
        todolist = TodoList.objects.get(id=pk)
        todolist.delete()
        return redirect(to='/')

def editTodolist(request, pk):
    obj = TodoList.objects.get(id=pk)
    if request.method == 'POST':
        todolist = TodoListForm(request.POST, instance=obj)
        todolist.save()
        return redirect(to='/')
    params = {
        'form': TodoListForm(instance=obj),
        'id': pk,
    }
    return render(request, 'TODO/edit.html', params)