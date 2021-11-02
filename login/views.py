from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import hashlib
import json
from datetime import date, timedelta
from .models import Login, LogLogin


# Create your views here.
def login(request):
    if request.session.get('usuario'):
        return redirect('/home/saude/')

    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})


def valida_login(request):
    if request.session.get('usuario'):
        return redirect('/home/saude/')

    login = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = hashlib.sha256(senha.encode()).hexdigest()

    if '@' in login:
        l = Login.objects.filter(email=login).filter(senha=senha)
    else:
        l = Login.objects.filter(nome_acesso=login).filter(senha=senha)

    if len(l) == 0:
        return redirect('/auth/login/?status=1')
    elif len(l) > 0:
        log = LogLogin(login=l[0])
        log.save()
        request.session['usuario'] = l[0].id
        return redirect('/home/saude/')


def sair(request):
    request.session.flush()
    return redirect('/auth/login/?status=3')


def cadastro(request):
    if request.session.get('usuario'):
        return redirect('/home/saude/')

    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})


def valida_cadastro_login(request):
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

    return redirect('/auth/login/?status=4')


def valida_email(request):
    email = request.POST.get('email')
    email = email.replace(" ", "")
    if '@' in email:
        valida_email = Login.objects.filter(email=email)

        if valida_email:
            return HttpResponse(json.dumps({'status': '1'}))
        else:
            return HttpResponse(json.dumps({'status': '2'}))
    return HttpResponse(json.dumps({'status': '3'}))


def valida_usuario_login(request):
    nome_acesso = request.POST.get('nome_acesso')
    nome_acesso = nome_acesso.replace(" ", "")
    valida_nome_acesso = Login.objects.filter(nome_acesso=nome_acesso)
    if valida_nome_acesso:
        return HttpResponse(json.dumps({'status': '1'}))
    else:
        return HttpResponse(json.dumps({'status': '2'}))
