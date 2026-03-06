from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from .models import Programa, Curso, Estudiante, Inscripcion

class ProgramaModelTest(TestCase):
    def setUp(self):
        self.programa = Programa.objects.create(
            codigo='ING001',
            nombre='Ingeniería de Sistemas',
            duracion=10
        )

    def test_programa_string(self):
        self.assertEqual(str(self.programa), 'Ingeniería de Sistemas')

class CursoModelTest(TestCase):
    def setUp(self):
        self.programa = Programa.objects.create(
            codigo='ING001', nombre='Ingeniería', duracion=10
        )
        self.curso = Curso.objects.create(
            codigo='PRO101',
            nombre='Programación I',
            creditos=4,
            programa=self.programa
        )

    def test_curso_string(self):
        self.assertEqual(str(self.curso), 'Programación I')

class EstudianteModelTest(TestCase):
    def setUp(self):
        self.programa = Programa.objects.create(
            codigo='ING001', nombre='Ingeniería', duracion=10
        )
        self.estudiante = Estudiante.objects.create(
            nombre='Adiz Quintero',
            email='adiz@example.com',
            programa=self.programa
        )

    def test_estudiante_string(self):
        self.assertEqual(str(self.estudiante), 'Adiz Quintero (Ingeniería)')

class InscripcionModelTest(TestCase):
    def setUp(self):
        self.programa = Programa.objects.create(codigo='ING001', nombre='Ingeniería', duracion=10)
        self.curso = Curso.objects.create(codigo='PRO101', nombre='Programación I', creditos=4, programa=self.programa)
        self.estudiante = Estudiante.objects.create(nombre='Adiz Quintero', email='adiz@example.com', programa=self.programa)
        
    def test_inscripcion_unique(self):
        Inscripcion.objects.create(estudiante=self.estudiante, curso=self.curso)
        # Debe fallar por unique_together
        with self.assertRaises(Exception):
            Inscripcion.objects.create(estudiante=self.estudiante, curso=self.curso)
