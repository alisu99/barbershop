from django.shortcuts import render
from django.http import JsonResponse
from .models import Profissional, Servico, Agendamento, Horario, Disponibilidade
import datetime

def index(request):
    servicos = Servico.objects.all()
    proximos_dias = []
    data_atual = datetime.date.today()

    for i in range(12):
        dia_futuro = data_atual + datetime.timedelta(days=i)
        proximos_dias.append(dia_futuro.strftime("%Y-%m-%d"))

    context = {
        "servicos": servicos,
        "proximos_dias": proximos_dias,
    }

    return render(request, "index.html", context)

def verificar_profissionais(request):
    data = request.GET.get('data')
    data_formatada = datetime.datetime.strptime(data, "%Y-%m-%d").date()
    profissionais_disponiveis = Profissional.objects.filter(disponibilidade__data=data_formatada).distinct()

    profissionais = list(profissionais_disponiveis.values('id', 'nome'))
    return JsonResponse(profissionais, safe=False)

def verificar_horarios(request):
    profissional_id = request.GET.get('profissional')
    data = request.GET.get('data')
    data_formatada = datetime.datetime.strptime(data, "%Y-%m-%d").date()

    horarios_disponiveis = Horario.objects.filter(
        disponibilidade__profissional_id=profissional_id,
        disponibilidade__data=data_formatada
    ).exclude(
        agendamento__profissional_selecionado_id=profissional_id,
        agendamento__data=data_formatada
    )

    horarios = list(horarios_disponiveis.values('id', 'horario'))
    return JsonResponse(horarios, safe=False)

def agendar(request):
    if request.method == 'POST':
        servico_id = request.POST['servico']
        profissional_id = request.POST['profissional']
        horario_id = request.POST['horario']
        data = request.POST['data']
        nome_cliente = request.POST['nome_cliente']
        telefone_cliente = request.POST['telefone_cliente']
        email_cliente = request.POST['email_cliente']

        data_formatada = datetime.datetime.strptime(data, "%Y-%m-%d").date()

        agendamento = Agendamento(
            servico_selecionado_id=servico_id,
            profissional_selecionado_id=profissional_id,
            horario_selecionado_id=horario_id,
            data=data_formatada,
            nome_cliente=nome_cliente,
            telefone_cliente=telefone_cliente,
            email_cliente=email_cliente
        )
        agendamento.save()

        return JsonResponse({"mensagem": "Agendamento realizado com sucesso."}, status=201)

    return JsonResponse({"mensagem": "Método não permitido."}, status=405)
