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

class PerteneceACurso(models.Model):
    rut = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=False, blank=False)
    rol = models.CharField(max_length=20)

class Coevaluacion(models.Model):
    nombre=models.CharField(max_length=60)
    id_curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    fecha_inicio= models.DateTimeField()
    fecha_termino=models.DateTimeField()
    status=models.BooleanField() #Abierto True Cerrado False
    #Falta agregar las preguntas

class Equipos(models.Model):
    nombre=models.CharField(max_length=60)
    rut_alumno=models.ForeignKey(User, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    actual= models.BooleanField()


class Preguntas(models.Model):
    id_coev = models.ForeignKey(Coevaluacion, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    texto_pregunta = models.CharField(max_length=200)
    num_pregunta = models.IntegerField()
    tipo_pregunta = models.CharField(max_length=20) #pregunta de texto o seleccion
    ponderacion = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    respuesta = models.CharField(max_length=200)
    a =0

def validate_decimals(value):
    try:
        return round(float(value), 2)
    except:
        raise ValidationError(
            ('%(value)s is not an integer or a float  number'),
            params={'value': value},
        )

class AlumnoTieneCoevaluacion(models.Model):
    rut = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=False, blank=False)
    id_coev = models.ForeignKey(Coevaluacion, on_delete=models.CASCADE, null=False, blank=False)
    contestada = models.BooleanField()
    nota = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(7), validate_decimals])
