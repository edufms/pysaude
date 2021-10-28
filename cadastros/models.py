from django.db import models


class Usuarios(models.Model):
    choices = {
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('I', 'Indefinido'),
        ('NI', 'Não informado')
    }
    nome_completo = models.CharField(max_length=150)
    nome_social = models.CharField(max_length=150)
    sexo = models.CharField(max_length=15, choices=choices)
    cpf = models.CharField(max_length=11)
    cns = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    nome_mae = models.CharField(max_length=150)
    nome_pai = models.CharField(max_length=150)
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=255)
    num_endereco = models.IntegerField()
    complemento = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)
    ponto_referencias = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)


class Telefones(models.Model):
    choices = {
        ('f', 'Fixo'),
        ('c', 'Celular'),
        ('co', 'Comercial'),
        ('r', 'Recado')
    }
    usuario_id = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING)
    tipo_telefone = models.CharField(max_length=10, choices=choices)
    num_telefone = models.CharField(max_length=15)


class CBOS(models.Model):
    sigla = models.CharField(max_length=6)
    descricao = models.CharField(max_length=150)


class Especialidades(models.Model):
    descricao = models.CharField(max_length=150)
    cbo = models.ForeignKey(CBOS, on_delete=models.DO_NOTHING)


class Profissionais(models.Model):
    nome_completo = models.CharField(max_length=150)
    nome_social = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11)
    cns = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    nome_mae = models.CharField(max_length=150)
    nome_pai = models.CharField(max_length=150)
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=255)
    num_endereco = models.IntegerField()
    complemento = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    ponto_referencias = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)


class DocumentosRegistro(models.Model):
    sigla = models.CharField(max_length=20)
    nome_documento = models.CharField(max_length=255)


class EspecProfissionais(models.Model):
    id_specialidade = models.ForeignKey(
        Especialidades, on_delete=models.DO_NOTHING)
    id_rofissional = models.ForeignKey(
        Profissionais, on_delete=models.DO_NOTHING)
    id_documento_registro = models.ForeignKey(
        DocumentosRegistro, on_delete=models.DO_NOTHING)
    num_registro = models.CharField(max_length=15)


class TiposExames(models.Model):
    descricao = models.CharField(max_length=255)


class Exames(models.Model):
    descricao = models.CharField(max_length=150)
    sigla = models.CharField(max_length=5)
    id_tipo_exame = models.ForeignKey(
        TiposExames, on_delete=models.DO_NOTHING)
