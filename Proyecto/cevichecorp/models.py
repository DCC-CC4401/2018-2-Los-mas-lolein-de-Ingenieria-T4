from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=60)
    codigo = models.CharField(max_length=15)
    seccion = models.IntegerField()
    anho = models.IntegerField()
    semestre = models.IntegerField()
    class Meta:
        unique_together = (('codigo','seccion','anho','semestre'))

EST = "ESTUDIANTE"
PROF = "PROFESOR"
AUX = "PROFESOR AUXILIAR"
AYUD = "AYUDANTE"

ROL_CHOICES = (
    (EST, "Estudiante"),
    (PROF, "Profesor"),
    (AUX, "Profesor auxiliar"),
    (AYUD, "Ayudante"),
)

class PerteneceACurso(models.Model):
    rut = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=False, blank=False)
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)
    class Meta:
        unique_together = (('rut','id_curso'))

class Coevaluacion(models.Model):
    nombre=models.CharField(max_length=60)
    id_curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    fecha_inicio= models.DateTimeField()
    fecha_termino=models.DateTimeField()
    status=models.IntegerField() #prepublicado 0 abierta 1, cerrada 2, publicada 3
    class Meta:
        unique_together = (('nombre','id_curso'))

class Equipos(models.Model):
    nombre=models.CharField(max_length=60)
    rut_alumno=models.ForeignKey(User, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    actual= models.BooleanField()
    class Meta:
        unique_together = (('nombre','rut_alumno','id_curso'))

class Preguntas(models.Model):
    id_coev = models.ForeignKey(Coevaluacion, on_delete=models.CASCADE)
    texto_pregunta = models.CharField(max_length=200)
    num_pregunta = models.IntegerField()
    tipo_pregunta = models.CharField(max_length=20) #pregunta de texto o seleccion
    ponderacion = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    class Meta:
        unique_together = (('id_coev','num_pregunta','texto_pregunta'))

class RespuestasAlumnos(models.Model):
    id_pregunta = models.ForeignKey(Preguntas, on_delete=models.CASCADE)
    rut_desde = models.ForeignKey(User, on_delete=models.CASCADE, related_name="desde")
    rut_objetivo = models.ForeignKey(User, on_delete=models.CASCADE, related_name="para")
    respuesta = models.CharField(max_length=150)
    nota = models.FloatField()
    class Meta:
        unique_together = (('id_pregunta','rut_desde','rut_objetivo'))


def validate_decimals(value):
    try:
        return round(float(value), 2)
    except:
        raise ValidationError(
            ('%(value)s is not an integer or a float  number'),
            params={'value': value},
        )



class AlumnoTieneCoevaluacion(models.Model):
    id_curso = models.ForeignKey(PerteneceACurso, on_delete=models.CASCADE, null=False, blank=False)
    id_coev = models.ForeignKey(Coevaluacion, on_delete=models.CASCADE, null=False, blank=False)
    contestada = models.BooleanField(default=False)
    notapromedio = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(7), validate_decimals])
    class Meta:
        unique_together = (('id_curso','id_coev'))

