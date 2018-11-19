from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.http import HttpResponseRedirect



# Create your views here.
def index(request):
    #si el usuario ya inició sesión:
    if request.user.is_authenticated:
        usuarioactual = request.user
        nombre= request.user.get_full_name()
        cursosusuario= PerteneceACurso.objects.filter(rut=usuarioactual)
        listaids=list()
        for curso in cursosusuario:
             listaids.append (AlumnoTieneCoevaluacion.objects.get(id_curso= curso).pk)
        coevaluaciones = AlumnoTieneCoevaluacion.objects.filter(pk__in=listaids )
        return render(request, 'home-vista-alumno.html',{'coev': coevaluaciones,'cursos':cursosusuario,'usuario': nombre})

    else:
        #si el usuario esta iniciando sesion / respondió el formulario
        if request.method =='POST':
            username = request.POST['rut']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            #si el usuario existe y esta bien su contraseña
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/")
            #si no, le mandamos este mensaje en el contexto
            else:
               return render(request,'login.html',{'mensaje':'Error, usuario o contraseña inválida'})
        #si no esta iniciada su sesión lo mandamos a iniciar sesion.
        else :
            return render(request,'login.html')


def out(request):
    logout(request)
    return HttpResponseRedirect("/")
