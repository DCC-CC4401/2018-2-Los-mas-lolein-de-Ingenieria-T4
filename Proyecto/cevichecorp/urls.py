from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
  #  path('perfil/', views.consultar, name='perfil'),
 ]