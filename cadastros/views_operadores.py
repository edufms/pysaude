from django.shortcuts import render, redirect
from django.http import HttpResponse
import hashlib
from datetime import date, timedelta
from .models import Usuarios
from login.models import Login


def cadastro_operadores(request):
    status = request.GET.get('status')
    return render(request, 'cad_operadores.html', {'status': status})


def valida_operador(request):

    if request.session.get('usuario'):
        return redirect('/home/saude/')

    nome_completo = request.POST.get('nome_completo')
    nome_acesso = request.POST.get('nome_acesso')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    cadastro_email = Login.objects.filter(email=email)
    if cadastro_email:
        return redirect('/auth/cadastro/?status=1')

    cadastro_nome_acesso = Login.objects.filter(nome_acesso=nome_acesso)
    if cadastro_nome_acesso:
        return redirect('/auth/cadastro/?status=2')

    senha = hashlib.sha256(senha.encode()).hexdigest()
    validade_senha = 180
    data_expiracao = date.today() + timedelta(days=validade_senha)
    status = 1

    novo_cadastro = Login(nome_completo=nome_completo, nome_acesso=nome_acesso,
                          email=email, senha=senha, validade_senha=validade_senha, data_expiracao=data_expiracao, status=status
                          )
    novo_cadastro.save()

    return redirect('/home/saude/cadastro_operadores/?status=1')
    pass


def pesquisa_operadores(request):
    pass
