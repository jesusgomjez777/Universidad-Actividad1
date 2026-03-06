from django.shortcuts import render
from django.http import HttpResponse
from .models import Programa, Curso, Estudiante

def lista_programas(request):
    """Vista para listar todos los programas académicos"""
    programas = Programa.objects.all()
    contexto = {'programas': programas}
    return render(request, 'academia/programas.html', contexto)

def lista_cursos(request):
    """Vista para listar todos los cursos"""
    cursos = Curso.objects.all()
    contexto = {'cursos': cursos}
    return render(request, 'academia/cursos.html', contexto)

def lista_estudiantes(request):
    """Vista para listar todos los estudiantes"""
    estudiantes = Estudiante.objects.all()
    contexto = {'estudiantes': estudiantes}
    return render(request, 'academia/estudiantes.html', contexto)
