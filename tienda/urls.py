from django.urls import path
from . import views

urlpatterns = [
    path('programas/', views.lista_programas, name='programas'),
    path('cursos/', views.lista_cursos, name='cursos'),
    path('estudiantes/', views.lista_estudiantes, name='estudiantes'),
]
