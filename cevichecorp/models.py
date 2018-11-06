from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=60)
    codigo = models.CharField(max_length=15, primary_key=True)
    seccion = models.IntegerField(primary_key=True)
    anho = models.IntegerField(primary_key=True)
    semestre = models.IntegerField(primary_key=True)

class PerteneceACurso(models.Model):
    rut = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    codigo = models.ForeignKey(Curso, on_delete=models.CASCADE, null=False, blank=False, related_name='codigo')
    seccion = models.ForeignKey(Curso, on_delete=models.CASCADE, null=False, blank=False, related_name='seccion')
    anho = models.ForeignKey(Curso, on_delete=models.CASCADE, null=False, blank=False, related_name='anho')
    semestre = models.ForeignKey(Curso, on_delete=models.CASCADE, null=False, blank=False, related_name='semestre')
    rol = models.CharField(max_length=20)

class Coevaluacion(models.Model):
    nombre=models.Charfield(max_length=60,primary_key=True)
    nombre_curso=models.ForeignKey(Curso,related_name='nombre',on_delete=models.CASCADE)
    codigo_curso = models.ForeignKey(Curso,related_name='codigo',on_delete=models.CASCADE)
    seccion_curso = models.ForeignKey(Curso,related_name='seccion',on_delete=models.CASCADE)
    amho_curso = models.ForeignKey(Curso,related_name='anho',on_delete=models.CASCADE)
    semestre_curso = models.ForeignKey(Curso,related_name='semestre',on_delete=models.CASCADE)
    fecha_inicio= models.DateTimeField()
    fecha_termino=models.DateTimeField()
    estatus=models.BooleanField() #Abierto True Cerrado False

class Equipos(models.Model):
     nombre=models.CharField(max_length=60,primary_key=True)
     rut_alumno=models.ForeignKey(User,related_name='username')
     nombre_curso = models.ForeignKey(Curso, related_name='nombre', on_delete=models.CASCADE)
     codigo_curso = models.ForeignKey(Curso, related_name='codigo', on_delete=models.CASCADE)
     seccion_curso = models.ForeignKey(Curso, related_name='seccion', on_delete=models.CASCADE)
     amho_curso = models.ForeignKey(Curso, related_name='anho', on_delete=models.CASCADE)
     semestre_curso = models.ForeignKey(Curso, related_name='semestre', on_delete=models.CASCADE)
     actual= models.BooleanField()


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
    codigo = models.ForeignKey(Curso, on_delete=models.CASCADE, null=False, blank=False, related_name='codigo')
    seccion = models.ForeignKey(Curso, on_delete=models.CASCADE, null=False, blank=False, related_name='seccion')
    anho = models.ForeignKey(Curso, on_delete=models.CASCADE, null=False, blank=False, related_name='anho')
    semestre = models.ForeignKey(Curso, on_delete=models.CASCADE, null=False, blank=False, related_name='semestre')
    nombre_coev = models.ForeignKey(Coevaluacion, on_delete=models.CASCADE, null=False, blank=False,
                                    related_name='nombre')
    contestada = models.BooleanField()
    nota = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(7), validate_decimals])

