from django.urls import path
from . import views

app_name = "tienda"

urlpatterns = [
    path("", views.home, name="home"),
    path("programas/", views.lista_programa, name="lista_programa"),
    path("cursos/", views.lista_curso, name="lista_curso"),
    path("estudiantes/", views.lista_estudiante, name="lista_estudiante"),
]