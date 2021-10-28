from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import hashlib
from .models import Login


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
        request.session['usuario'] = l[0].id
        return redirect('/home/saude/')

def sair(request):
    request.session.flush()
    return redirect('/auth/login/?status=3')

        