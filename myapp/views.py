from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def saludar(request):
    return HttpResponse('<h1>Hello Word</h1>')

def about(request):
    return HttpResponse('About')