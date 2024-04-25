from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Index(request):
    return HttpResponse("Index page")


def saludar(request, username):
    return HttpResponse('<h1>Hello %s</h1>' % username)

def about(request):
    return HttpResponse('About')