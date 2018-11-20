from django.contrib import admin

from cevichecorp.models import Curso, PerteneceACurso, Coevaluacion, Equipos, Preguntas, AlumnoTieneCoevaluacion, RespuestasAlumnos
# Register your models here.
admin.site.register(Curso)
admin.site.register(PerteneceACurso)
admin.site.register(Coevaluacion)
admin.site.register(Equipos)
admin.site.register(Preguntas)
admin.site.register(AlumnoTieneCoevaluacion)
admin.site.register(RespuestasAlumnos)