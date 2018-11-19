from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'home-vista-alumno.html')
    else:
        if request.method =='POST':
            username = request.POST['rut']
            password = request.POST['password ']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                return render(request, 'home-vista-alumno.html')

            else:
                return render(request,'login.html')
        else :
            return render(request,'login.html')


def curso(request):
    cursos = PerteneceACurso.objects.all()
    user_name = user.get_username() #Puede hacer con un filter
    for curso in cursos:
        if user_name==curso.rut:
            #recuperar curso



