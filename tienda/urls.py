from django.urls import path
from . import views

app_name = "tienda"

urlpatterns = [
    path("", views.home, name="home"),
    path("programas/", views.lista_programa, name="lista_programa"),
    path("programas/<str:pk>/", views.detalle_programa, name="detalle_programa"),
    path("cursos/", views.lista_curso, name="lista_curso"),
    path("cursos/<str:pk>/", views.detalle_curso, name="detalle_curso"),
    path("estudiantes/", views.lista_estudiante, name="lista_estudiante"),
    path("estudiantes/<str:pk>/", views.detalle_estudiante, name="detalle_estudiante"),
]