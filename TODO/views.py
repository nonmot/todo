from django.shortcuts import render
from .models import TodoList, Task
from .forms import TodoListForm, TaskForm
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.

@login_required
def home(request):
    todolist = TodoList.objects.filter(owner=request.user)
    todaytask = Task.objects.filter(owner=request.user).filter(deadline=datetime.date.today())
    params = {
        'todolist': todolist,
        'todaytask': todaytask,
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

# CRUD for TodoList
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
    return render(request, 'TODO/editlist.html', params)

# CRUD for Task
def newTask(request, pk):
    if request.method == 'POST':
        obj = Task()
        obj.owner = request.user
        # Taskインスタンスのtodolistに現在のtodolistを設定
        obj.todolist = TodoList.objects.get(id=pk)
        newtask = TaskForm(request.POST, instance=obj)
        newtask.save()
        #リダイレクト先に元のTodolist
        redirect_path = '/task/' + str(pk)
        return redirect(to=redirect_path)
    else:
        form = TaskForm()
    params = {
        'form': form,
        'id': pk,
    }
    return render(request, 'TODO/newtask.html', params)

def deleteTask(request, listpk, taskpk):
    if request.method == 'POST':
        task = Task.objects.filter(id=taskpk)
        task.delete()
        redirect_path = '/task/' + str(listpk)
        return redirect(to=redirect_path)

def editTask(request, listpk, taskpk):
    obj = Task.objects.get(id=taskpk)
    if request.method == 'POST':
        task = TaskForm(request.POST, instance=obj)
        task.save()
        redirect_url = '/task/' + str(listpk)
        return redirect(to=redirect_url)
    params = {
        'form': TaskForm(instance=obj),
        'listpk': listpk,
        'taskpk': taskpk,
    }
    return render(request, 'TODO/edittask.html', params)