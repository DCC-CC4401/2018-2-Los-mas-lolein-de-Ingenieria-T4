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
            if AlumnoTieneCoevaluacion.objects.filter(id_curso=curso).exists():
                coevs = AlumnoTieneCoevaluacion.objects.filter(id_curso= curso)
                for coev in coevs:
                    listaids.append(coev.pk)
        coevaluaciones = AlumnoTieneCoevaluacion.objects.filter(pk__in=listaids )

        dic = {
            'coev': coevaluaciones,
            'cursos':cursosusuario,
            'usuario': nombre
        }
        return render(request, 'home-vista-alumno.html', dic)

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

def perfil(request):
    if request.user.is_authenticated:
        usuarioactual = request.user
        nombre = request.user.get_full_name()
        mail= usuarioactual.email
        cursos_usuario = PerteneceACurso.objects.filter(rut=usuarioactual)
        listaids = list()
        for curso in cursos_usuario:
            if AlumnoTieneCoevaluacion.objects.filter(id_curso=curso).exists():
                coevs = AlumnoTieneCoevaluacion.objects.filter(id_curso= curso)
                for coev in coevs:
<<<<<<< HEAD
                    listaids.append(coev.pk)
        coevaluaciones = AlumnoTieneCoevaluacion.objects.filter(pk__in=listaids)
=======
                    listaids.append (coev.pk)
        coevaluaciones = AlumnoTieneCoevaluacion.objects.filter(pk__in=listaids )
>>>>>>> 4d872269063809a8539f90be72f7013679060432
        dicti = {
            'usuario':nombre,
            'rut': usuarioactual,
            'mail':mail,
            'cursos': cursos_usuario,
            'coevs': coevaluaciones
            }
        return render(request, "perfil-vista-dueno.html", dicti)

    else:
        return render(request, 'login.html', {'mensaje': 'Debe iniciar sesión para ingresar.'})

def cambioContrasena(request):
    if request.user.is_authenticated:
        usuarioactual = request.user
        nombre = request.user.get_full_name()
        mail = usuarioactual.email
        old_pass = request.POST['passOld']
        new_pass = request.POST['passNew']
        new_pass_confirm = request.POST['passNewConfirm']
        user = authenticate(request, username=usuarioactual, password=old_pass)
        if user is not None and new_pass== new_pass_confirm:
            usuarioactual.set_password(new_pass_confirm)
            usuarioactual.save()
            user = authenticate(request, username=usuarioactual, password=new_pass_confirm)
            if user is not None:
                return render(request, "perfil-vista-dueno.html", {'usuario':nombre,'rut':usuarioactual, 'mail':mail, 'mensaje': 'Se ha actualizado de manera exitosa la contraseña.'})
            else:
                return render(request, 'login.html', {'mensaje': 'Debe iniciar sesión para ingresar.'})
        else:
            return render(request, "perfil-vista-dueno.html", {'usuario':nombre,'rut':usuarioactual, 'mail':mail, 'mensaje': 'La contraseña ingresada es incorrecta o ambas contraseñas nuevas no coinciden'})
    else:
        return render(request, 'login.html', {'mensaje': 'Debe iniciar sesión para ingresar.'})


def coevaluacion(request):
    if request.user.is_authenticated:
        usuario=request.user.get_full_name
        id= request.GET.get('coev')
        coev = None
        if id is not None:
            coev= AlumnoTieneCoevaluacion.objects.get(pk=int(id))
        equipo= Equipos.objects.get(rut_alumno=request.user,actual=True)
        nombre=equipo.nombre
        mates=Equipos.objects.exclude(rut_alumno=request.user).filter(nombre=nombre, actual=True)
        if request.GET.get('alumno') is not None:
            correspondiente=User.objects.get(username=request.GET.get('alumno'))
        else :
            correspondiente=None

        return render(request, 'coevaluacion-vista-alumno.html',{'usuario':usuario,'coev':coev,'mates':mates,'correspondiente':correspondiente,'id':id})


    else:
        return render(request, 'login.html', {'mensaje': 'Debe iniciar sesión para ingresar.'})