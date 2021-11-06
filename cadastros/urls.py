
from django.contrib import admin
from django.urls import path
from . import views, views_operadores

urlpatterns = [
    path('cadastro_usuarios/', views.cadastro_usuarios,
         name='cadastro_usuarios'),  # formulario de cadastro do usuario
    # validacao do formulario do cadastro de usuario
    path('valida_usuario/', views.valida_usuario, name='valida_usuario'),
    path('pesquisa_usuarios/', views.pesquisa_usuarios, name='pesquisa_usuarios'),
    path('cadastro_operadores/', views_operadores.cadastro_operadores,
         name='cadastro_operadores'),  # formulario de cadastro do usuario
    # validacao do formulario do cadastro de usuario
    path('valida_operador/', views_operadores.valida_operador,
         name='valida_operador'),
    path('pesquisa_operadores/', views_operadores.pesquisa_operadores,
         name='pesquisa_operadores'),
]
