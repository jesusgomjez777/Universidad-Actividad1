from django.shortcuts import render
from django.http import HttpResponse
from .models import Programa, Curso, Estudiante
from django.shortcuts import render, get_object_or_404

def home(request):
    return render(request, "tienda/home.html", {})

def detalle_programa(request, pk):
    programa = get_object_or_404(Programa, pk=pk)
    contexto = {"programa": programa}
    return render(request, "tienda/detalle_programa.html", contexto)

def lista_programa(request):
    """Vista para listar todos los programas académicos"""
    programas = Programa.objects.all()
    contexto = {'programas': programas}
    return render(request, 'tienda/lista_programa.html', contexto)

def detalle_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    contexto = {"curso": curso}
    return render(request, "tienda/detalle_curso.html", contexto)

def lista_curso(request):
    """Vista para listar todos los cursos"""
    cursos = Curso.objects.all()
    contexto = {'cursos': cursos}
    return render(request, 'tienda/lista_curso.html', contexto)

def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    contexto = {"estudiante": estudiante}
    return render(request, "tienda/detalle_estudiante.html", contexto)

def lista_estudiante(request):
    """Vista para listar todos los estudiantes"""
    estudiantes = Estudiante.objects.all()
    contexto = {'estudiantes': estudiantes}
    return render(request, 'tienda/lista_estudiante.html', contexto)
