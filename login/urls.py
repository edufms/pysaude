
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('valida_login/', views.valida_login, name='valida_login'),
    path('sair/', views.sair, name='sair'),
    path('cadastro/', views.cadastro, name='cadastro_login'),
    path('valida_cadastro_login/', views.valida_cadastro_login,
         name='valida_cadastro_login'),
]
