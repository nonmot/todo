from django.urls import path
from. import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task/<int:pk>', views.task, name='task'),
    path('newlist/', views.newList, name='newlist'),
    path('newtask/<int:pk>', views.newTask, name="newtask"),
    path('deletelist/<int:pk>', views.deleteTodolist, name="deletelist"),
    path('editlist/<int:pk>', views.editTodolist, name="editlist"),
    path('deletetask/<int:listpk>/<int:taskpk>', views.deleteTask, name="deletetask"),
    path('edittask/<int:listpk>/<int:taskpk>', views.editTask, name="edittask"),
]