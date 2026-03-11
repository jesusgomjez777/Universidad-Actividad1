from django.shortcuts import render
from django.http import HttpResponse
from .models import Programa, Curso, Estudiante

def home(request):
    return render(request, "tienda/home.html", {})

def lista_programa(request):
    """Vista para listar todos los programas académicos"""
    programas = Programa.objects.all()
    contexto = {'programas': programas}
    return render(request, 'tienda/lista_programa.html', contexto)

def lista_curso(request):
    """Vista para listar todos los cursos"""
    cursos = Curso.objects.all()
    contexto = {'cursos': cursos}
    return render(request, 'tienda/lista_curso.html', contexto)

def lista_estudiante(request):
    """Vista para listar todos los estudiantes"""
    estudiantes = Estudiante.objects.all()
    contexto = {'estudiantes': estudiantes}
    return render(request, 'tienda/lista_estudiante.html', contexto)
