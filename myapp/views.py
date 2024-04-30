from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_list_or_404
from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request, "index.html")

def about(request):
    return render(request, 'about.html')

def saludar(request, username):
    return HttpResponse('<h1>Hello %s</h1>' % username)

def proyectos(request):
    proyectos = list(Project.objects.values())
    return render(request, 'proyectos.html')

def tasks(request):
    #task = Task.objects.get(title=title)
    return render(request, 'tasks.html')