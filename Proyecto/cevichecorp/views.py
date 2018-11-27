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
        cursosusuario = sorted(cursosusuario, reverse=True, key=getKeyCursos)
        listaids=list()
        for curso in cursosusuario:
            if AlumnoTieneCoevaluacion.objects.filter(id_curso=curso).exists():
                coevs = AlumnoTieneCoevaluacion.objects.filter(id_curso= curso)
                for coev in coevs:
                    listaids.append(coev.pk)
        coevaluaciones = AlumnoTieneCoevaluacion.objects.filter(pk__in=listaids )
        coevaluaciones = sorted(coevaluaciones, reverse=True, key=getKeyCoevs)
        coevaluaciones=coevaluaciones[:10]

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

def getKeyCursos(elem):
    return [elem.id_curso.anho, elem.id_curso.semestre]

def getKeyCoevs(elem):
    return elem.id_coev.fecha_inicio

def perfil(request):
    if request.user.is_authenticated:
        usuarioactual = request.user
        nombre = request.user.get_full_name()
        mail= usuarioactual.email
        cursos_usuario = PerteneceACurso.objects.filter(rut=usuarioactual)
        cursos_usuario = sorted(cursos_usuario, reverse=True, key=getKeyCursos)
        listaids = list()
        for curso in cursos_usuario:
            if AlumnoTieneCoevaluacion.objects.filter(id_curso=curso).exists():
                coevs = AlumnoTieneCoevaluacion.objects.filter(id_curso= curso)
                for coev in coevs:
                    listaids.append (coev.pk)
        coevaluaciones = AlumnoTieneCoevaluacion.objects.filter(pk__in=listaids )
        coevaluaciones = sorted(coevaluaciones, reverse=True, key=getKeyCoevs)
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
        respuestas=None
        mensaje = ""
        if request.method == 'POST':
             estudiante = User.objects.get(username=request.POST['estudiante'])
             pregunta = Preguntas.objects.get()
             new_preguntas = RespuestasAlumnos(id_pregunta=pregunta, rut_desde=request.user, rut_objetivo=estudiante,
                                               respuesta="blahblah", nota=1.0)
             new_preguntas.save()
             mensaje = "Se ha envidado tu coevaluacioń"
             respuestas=new_preguntas


        usuario=request.user.get_full_name
        id= request.GET.get('coev')
        coev = None
        if id is not None:
            coev = AlumnoTieneCoevaluacion.objects.get(pk=int(id))
        equipo= Equipos.objects.get(rut_alumno=request.user,actual=True)
        nombre=equipo.nombre
        mates=Equipos.objects.exclude(rut_alumno=request.user).filter(nombre=nombre, actual=True)
        if request.GET.get('alumno') is not None:
            correspondiente=User.objects.get(username=request.GET.get('alumno'))
        else :
            correspondiente=None
        return render(request, 'coevaluacion-vista-alumno.html',{'usuario':usuario,'coev':coev,'mates':mates,'correspondiente':correspondiente,'id':id,'mensaje':mensaje,'res':respuestas})
     else:
        return render(request, 'login.html', {'mensaje': 'Debe iniciar sesión para ingresar.'})

def curso(request, id_curso):
    #if request.method == 'POST':
        #new_coevaluacion= Coevaluacion(nombre=request.POST[''] ,id_curso=,fecha_inicio=,fecha_termino=, estatus='0')
    if request.user.is_authenticated:
        curso = PerteneceACurso.objects.get(pk=id_curso)
        rut = curso.rut
        usuario = request.user.get_full_name
        nombre_curso = curso.id_curso.nombre
        codigo_curso = curso.id_curso.codigo
        seccion_curso = curso.id_curso.seccion
        anho_curso = curso.id_curso.anho
        semestre_curso = curso.id_curso.semestre
        rol = curso.rol

        if rol== 'alumno':
            listaids = list()
            if AlumnoTieneCoevaluacion.objects.filter(id_curso=curso).exists():
                coevs = AlumnoTieneCoevaluacion.objects.filter(id_curso=curso)
                for coev in coevs:
                    listaids.append(coev.pk)
            coevaluaciones = AlumnoTieneCoevaluacion.objects.filter(pk__in=listaids)
            dict = {
                'nombre': nombre_curso,
                'codigo': codigo_curso,
                'seccion': seccion_curso,
                'anho': anho_curso,
                'semestre': semestre_curso,
                'rol': rol,
                'rut': rut,
                'coevs': coevaluaciones,
                'usuario': usuario
            }
            return render(request, 'curso-vista-alumno.html', dict)
        else :
            coevaluaciones=AlumnoTieneCoevaluacion.objects.all()
            coevs=Coevaluacion.objects.filter(id_curso=curso.id_curso)
            equipos= Equipos.objects.filter(id_curso=curso.id_curso)
            listaids2=list()
            for equipo in equipos:
                if  equipo.nombre not in listaids2:
                    listaids2.append(equipo.nombre)

            dict = {
                'curso':curso.id_curso,
                'nombre': nombre_curso,
                'codigo': codigo_curso,
                'seccion': seccion_curso,
                'anho': anho_curso,
                'semestre': semestre_curso,
                'rol': rol,
                'rut': rut,
                'coevs': coevs,
                'usuario': usuario,
                'equipos':equipos,
                'nombre_equipo':listaids2,
                'coevaluaciones': coevaluaciones
            }
            return render(request, 'curso-vista-alumno.html', dict)

    else:
        return render(request, 'login.html', {'mensaje': 'Debe iniciar sesión para ingresar.'})

def nuevaCoevaluacion(request,id_curso):
    curso = Curso.objects.get(pk=id_curso)
    usuario = request.user.get_full_name
    dict={'id_curso':curso,'usuario':usuario}
    return render(request, 'nueva-coevaluacion.html',dict)

def guardarCoevaluacion(request,id_curso):

    nombre_coev = request.POST['nombreCoev']
    curso_class = Curso.objects.get(pk=id_curso)
    fechainicio = request.POST['fechainicio']
    fechatermino = request.POST['fechatermino']
    status = request.POST['status']
    coev = Coevaluacion(nombre=nombre_coev, id_curso=curso_class, fecha_inicio=fechainicio, fecha_termino=fechatermino, status=status)
    coev.save()
    return curso(request,id_curso)
