
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_usuarios/', views.cadastro_usuarios, name='cadastro_usuarios'), #formulario de cadastro do usuario
    path('valida_usuario/', views.valida_usuario, name='valida_usuario'), #validacao do formulario do cadastro de usuario
    path('pesquisa_usuarios/', views.pesquisa_usuarios, name='pesquisa_usuarios'),
]
