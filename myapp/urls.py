from django.urls import path
from . import views

urlpatterns = [
    path('', views.saludar),
    path('about/', views.about)
]