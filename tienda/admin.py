from django.contrib import admin
from .models import Programa, Curso, Estudiante, Inscripcion

@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'duracion']
    search_fields = ['nombre', 'codigo']
    list_filter = ['duracion']

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'creditos', 'programa']
    list_filter = ['programa', 'creditos']
    search_fields = ['nombre', 'codigo']

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'programa', 'fecha_matricula']
    list_filter = ['programa', 'fecha_matricula']
    search_fields = ['nombre', 'email']

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ['estudiante', 'curso', 'nota', 'fecha_inscripcion']
    list_filter = ['curso__programa', 'fecha_inscripcion']
    search_fields = ['estudiante__nombre', 'curso__nombre']
