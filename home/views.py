from django.http.response import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.


def saude(request):
    if request.session.get('usuario'):
        return render(request, 'saude.html')
    else:
        return redirect('/auth/login/?status=2')


def index(request):
    if request.session.get('usuario'):
        return render(request, 'saude.html')
    else:
        return redirect('/auth/login/')
