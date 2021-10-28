from django.db import models

# Create your models here.

class Login(models.Model):
    nome_completo = models.CharField(max_length=100)
    nome_acesso = models.CharField(max_length=16)
    email = models.EmailField()
    senha = models.CharField(max_length=64)
    validade_senha = models.IntegerField()
    data_expiracao = models.DateField(auto_now_add=True)
    status = models.IntegerField()

class LogLogin(models.Model):
    login = models.ForeignKey(Login,on_delete=models.DO_NOTHING)
    data_login = models.DateTimeField(auto_now_add=True)

