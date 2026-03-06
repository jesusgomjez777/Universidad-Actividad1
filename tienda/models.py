from django.db import models

class Programa(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    duracion = models.PositiveSmallIntegerField(help_text="En semestres")

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)
    fecha_matricula = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.programa})"

class Curso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    creditos = models.PositiveSmallIntegerField()
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name='cursos')

    def __str__(self):
        return self.nombre

class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["estudiante", "curso"], name="unique_estudiante_curso"
            )
        ]

    def __str__(self):
        return f"{self.estudiante} - {self.curso}"

