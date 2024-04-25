from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_list_or_404

# Create your views here.
def Index(request):
    return HttpResponse("Index page")


def saludar(request, username):
    return HttpResponse('<h1>Hello %s</h1>' % username)

def about(request):
    return HttpResponse('About')

def proyectos(request):
    proyectos = list(Project.objects.values())
    return JsonResponse(proyectos, safe=False)

def tasks(request, title):
    task = Task.objects.get(title=title)
    return HttpResponse('tasks: %s' % task.title)