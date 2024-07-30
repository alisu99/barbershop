from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from admin_barbearia.models import *
import datetime
from django.views.decorators.http import require_GET
import locale
import calendar


locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

def index(request):
    servicos = Servico.objects.all()
    profissionais = Profissional.objects.filter(disponivel=True)
    horas = Horario.objects.all()
    data_atual = datetime.date.today()
    hora_atual = datetime.datetime.now().time()
    historicos = Agendamento.objects.filter(cliente_email=request.user.email if request.user.is_authenticated else None)
    if data_atual == datetime.date.today():
        horas_disponiveis = []
        for hora in horas:
            horario_formatado = hora.horario.replace("h", ":")
            try:
                horario_time = datetime.datetime.strptime(horario_formatado, "%H:%M").time()
                if horario_time >= hora_atual:
                    horas_disponiveis.append(hora)
                else:
                    print(f"Desconsiderando horário {hora.horario}.")
            except ValueError as e:
                print(f"Erro ao converter horário {hora.horario}: {e}")
        horas = horas_disponiveis

    proximos_dias = []
    for i in range(9):
        dia_futuro = data_atual + datetime.timedelta(days=i)
        dia_da_semana = calendar.day_name[dia_futuro.weekday()]
        dia_da_semana_sem_feira = dia_da_semana.replace('-feira', '').capitalize()
        proximos_dias.append((dia_futuro.strftime("%d/%m/%y"), dia_da_semana_sem_feira))

    context = {
        "horas": horas,
        "profissionais": profissionais,
        "servicos": servicos,
        "proximos_dias": proximos_dias,
        "historicos": historicos
    }

    return render(request, "index.html", context)

@require_GET
def verificar_disponibilidade(request):
    profissional_nome = request.GET.get("profissional_nome")
    data = request.GET.get("data")
    horario = request.GET.get("horario")

    data_formatada = datetime.datetime.strptime(data, "%d/%m/%y").date()
    disponivel = Agendamento.is_horario_disponivel(
        profissional_nome, data_formatada, horario
    )

    return JsonResponse({"disponivel": disponivel})

@require_GET
def horarios_disponiveis(request):
    profissional_nome = request.GET.get('profissional_nome')
    data_str = request.GET.get('data')
    data = datetime.datetime.strptime(data_str, "%d/%m/%y").date()

    # Obter todos os horários
    horarios = Horario.objects.all()

    # Filtrar horários que ainda não passaram, se for a data atual
    if data == datetime.date.today():
        hora_atual = datetime.datetime.now().time()
        horarios = [hora for hora in horarios if datetime.datetime.strptime(hora.horario.replace("h", ":"), "%H:%M").time() >= hora_atual]

    # Obter os horários já agendados
    horarios_agendados = Agendamento.objects.filter(
        profissional_selecionado=profissional_nome,
        data=data
    ).values_list('horario_selecionado', flat=True)

    # Filtrar horários disponíveis, excluindo os já agendados
    horarios_disponiveis = [hora for hora in horarios if hora.horario not in horarios_agendados]

    # Preparar a resposta
    horarios_disponiveis_dict = [{'id': hora.id, 'horario': hora.horario} for hora in horarios_disponiveis]

    return JsonResponse({'horarios': horarios_disponiveis_dict})


def agendar(request):
    if request.method == "POST":
        servico_id = request.POST.get("servico_id")
        profissional_id = request.POST.get("profissional_id")
        horario_id = request.POST.get("horario_id")
        data = request.POST.get("data")
        nome_cliente = request.POST.get("nome_cliente")
        telefone_cliente = request.POST.get("telefone_cliente")
        cliente_email = request.user.email if request.user.is_authenticated else None

        # Obtendo os nomes reais do serviço e profissional
        servico = Servico.objects.get(id=servico_id)
        profissional = Profissional.objects.get(id=profissional_id)
        horario = Horario.objects.get(id=horario_id)

        data_formatada = datetime.datetime.strptime(data, "%d/%m/%y").date()

        if Agendamento.is_horario_disponivel(profissional.nome, data_formatada, horario.horario):
            agendamento = Agendamento(
                servico_selecionado=servico.servico,  
                profissional_selecionado=profissional.nome,  
                horario_selecionado=horario.horario,  
                data=data_formatada,
                nome_cliente=nome_cliente,
                telefone_cliente=telefone_cliente,
                cliente_email=cliente_email
            )
            agendamento.save()
            return redirect('index')
        else:
            return JsonResponse({"success": False, "message": "Horário indisponível"})

    return JsonResponse({"success": False, "message": "Requisição inválida"})
