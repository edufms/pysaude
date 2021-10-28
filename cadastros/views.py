from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuarios
# Create your views here.


def cadastro_usuarios(request):
    status = request.GET.get('status')
    return render(request, 'cad_usuarios.html', {'status': status})


def valida_usuario(request):
    nome_completo = request.POST.get('inputNome')
    nome_social = ''
    sexo = request.POST.get('inputSexo')
    cpf = request.POST.get('inputCPF')
    cns = request.POST.get('inputCNS')
    data_nascimento = request.POST.get('inputDataNasc')
    nome_mae = request.POST.get('inputNomeMae')
    nome_pai = request.POST.get('inputNomePai')
    cep = request.POST.get('inputCEP')
    logradouro = request.POST.get('inputEndereco')
    num_endereco = request.POST.get('inputNumeroEndereco')
    complemento = request.POST.get('inputComplementoEndereco')
    bairro = request.POST.get('inputBairro')
    cidade = request.POST.get('inputCidade')
    estado = request.POST.get('inputEstado')
    ponto_referencias = request.POST.get('inputPontoReferencia')
    email = request.POST.get('inputEmail')
    print('-------------------------------------------------')
    print(request)
    usuario_cadastrado = Usuarios.objects.filter(cpf=cpf)

    if not usuario_cadastrado:
        usuario = Usuarios(nome_completo=nome_completo,
                           sexo=sexo,
                           cpf=cpf,
                           cns=cns,
                           data_nascimento=data_nascimento,
                           nome_mae=nome_mae,
                           nome_pai=nome_pai,
                           cep=cep,
                           logradouro=logradouro,
                           num_endereco=num_endereco,
                           complemento=complemento,
                           bairro=bairro,
                           cidade=cidade,
                           estado=estado,
                           ponto_referencias=ponto_referencias,
                           email=email)
        usuario.save()
    else:
        return redirect('/home/cadastros/cadastro_usuarios/?status=2')
    return redirect('/home/cadastros/cadastro_usuarios/?status=1')


def pesquisa_usuarios(request):
    if request.POST.get('nome_completo'):
        usuario_pesquisa = request.POST.get('nome_completo')
        if not request.POST.get('data_nascimento'):
            data_nascimento = None
        else:
            data_nascimento = request.POST.get('data_nascimento')
        cpf = request.POST.get('cpf')
        cns = request.POST.get('cns')
        nome_mae = request.POST.get('nome_mae')

        usuario = Usuarios.objects.filter(nome_completo__icontains=usuario_pesquisa,
                                          data_nascimento=data_nascimento,
                                          cpf=cpf,
                                          cns=cns,
                                          nome_mae=nome_mae)

        return render(request, 'pesq_usuarios.html', {'usuario': usuario})
    else:
        return render(request, 'pesq_usuarios.html')
