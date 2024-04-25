from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index),
    path('about/', views.about),
    path('saludar/<str:username>', views.saludar),
    path('proyectos/', views.proyectos),
    path('tasks/<str:title>', views.tasks),
]