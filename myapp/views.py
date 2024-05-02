from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def Index(request):
    title = 'Curso Django!!'
    return render(request, "index.html", {'title':title})

def about(request):
    username = 'alonso'
    return render(request, 'about.html', {'username' : username})

def saludar(request, username):
    return HttpResponse('<h1>Hello %s</h1>' % username)

def proyectos(request):
    #proyectos = list(Project.objects.values())
    proyectos = Project.objects.all()
    return render(request, 'projects/proyectos.html', {'proyectos' : proyectos})

def tasks(request):
    #task = Task.objects.get(title=title)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks' : tasks
        })
    
def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
        'form' : CreateNewTask()})
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('tasks')
    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form' : CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        render('proyectos')