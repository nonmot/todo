from django.urls import path
from. import views

urlpatterns = [
    path('', views.home, name='task'),
    path('task/<int:pk>', views.task, name='task'),
    path('newlist/', views.newList, name='newlist'),
    path('newtask/<int:pk>', views.newTask, name="newtask"),
]