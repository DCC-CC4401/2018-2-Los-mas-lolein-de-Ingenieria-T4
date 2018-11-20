from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('out/',views.out, name='out'),
    path('perfil/',views.perfil, name='perfil'),
    path('cambioContrasena/',views.cambioContrasena, name='cambioContrasena')
 ]