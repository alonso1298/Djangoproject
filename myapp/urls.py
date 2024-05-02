from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name="index"),
    path('about/', views.about, name="about"),
    path('saludar/<str:username>', views.saludar, name="hello"),
    path('proyectos/', views.proyectos, name="proyectos"),
    path('tasks/', views.tasks, name="tasks"),
    path('create_task/', views.create_task, name="create_tasks"),
    path('create_project/', views.create_project, name="create_project"),
]