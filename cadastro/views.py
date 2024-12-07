from django.shortcuts import render, redirect
from .models import Cadastrar, Agendamento
from django.contrib import messages

# Create your views here.

def paginaCadastro(request):
    if request.method == 'POST':

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        telefone = request.POST.get('telefone')
        peso = request.POST.get('peso')
        cep = request.POST.get('cep')
        cpf = request.POST.get('cpf')
        sexo = request.POST.get('sexo')
        tipo_sang = request.POST.get('tipo_sang')
        endereco = request.POST.get('endereco')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        uf = request.POST.get('uf')

        if not senha:
            messages.error(request, 'a senha não pode ser vazia.')
            return render(request, 'cadastro/cadastro.html')

        if Cadastrar.objects.filter(cpf=cpf).exists():
            messages.error(request, 'O CPF JÁ ESTÁ EM USO.')
        else:
            Cadastrar.objects.create(nome=nome,
                                     email=email,
                                     senha=senha,
                                     telefone=telefone,
                                     peso=peso,
                                     cep=cep,
                                     cpf=cpf,
                                     sexo=sexo,
                                     tipo_sang=tipo_sang,
                                     endereco=endereco,
                                     bairro=bairro,
                                     cidade=cidade,
                                     uf=uf)
            return redirect('login')
    return render(request,'cadastro/cadastro.html')


def paginaLogin(request):
    if request.method== 'POST':
        cpf = request.POST['cpf']
        senha = request.POST['senha']

        try:
            cadastro = Cadastrar.objects.get(cpf=cpf,  senha=senha)
            messages.success(request,f'Bem-vindo, {cadastro.nome}')
            return redirect('agendamento')
        except Cadastrar.DoesNotExist:
            messages.error(request, 'CPF ou senha inválidos.')

    return render(request, 'cadastro/login.html')

def inicial(request):
    return render(request, 'cadastro/home.html')

def dashboard(request):
    return render(request, 'cadastro/dashboard.html')

def historico(request):
    infomacao = Cadastrar.objects.all()
    dadosA = Agendamento.objects.all()
    return render(request, 'cadastro/historico.html', {'infomacao': infomacao, 'dadosA': dadosA })

def tabela(request):
    return render(request, 'cadastro/tabela.html')

def conf(request):
    return render(request, 'cadastro/conf.html')

def notificacao(request):
    return render(request, 'cadastro/Notificação.html')

def agendamento(request):
    infomacao = Cadastrar.objects.all()
    dadosA = Agendamento.objects.all()
    if  request.method == 'POST':
        nomeA = request.POST.get('nomeA')
        cpfA = request.POST.get('cpfA')
        agendamento_data = request.POST.get('agendamento_data')
        agendamento_hora = request.POST.get('agendamento_hora')
        Agendamento.objects.create(nomeA=nomeA,
                                 cpfA=cpfA,
                                 agendamento_hora=agendamento_hora,
                                 agendamento_data=agendamento_data)

    return render(request, 'cadastro/agendamento.html', {'infomacao': infomacao, 'dadosA': dadosA })
