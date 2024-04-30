from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_list_or_404
from django.shortcuts import render

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
    return render(request, 'proyectos.html', {'proyectos' : proyectos})

def tasks(request):
    #task = Task.objects.get(title=title)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks' : tasks
        })