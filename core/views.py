from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
import datetime
from django.views.decorators.http import require_GET
import locale
import calendar

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')


def index(request):
    servicos = Servico.objects.all()
    profissionais = Profissional.objects.all()
    horas = Horario.objects.all()
    data_atual = datetime.date.today()
    hora_atual = datetime.datetime.now().time()

    if data_atual == datetime.date.today():
        horas_disponiveis = []
        for hora in horas:
            horario_formatado = hora.horario.replace("h", ":")
            try:
                horario_time = datetime.datetime.strptime(horario_formatado, "%H:%M").time()
                if horario_time >= hora_atual:
                    horas_disponiveis.append(hora)
                else:
                    print(f"Desconsiderando horário {hora.horario}")
            except ValueError as e:
                print(f"Erro ao converter horário {hora.horario}: {e}")
        horas = horas_disponiveis

    proximos_dias = []

    for i in range(12):
        dia_futuro = data_atual + datetime.timedelta(days=i)
        dia_da_semana = calendar.day_name[dia_futuro.weekday()]
        dia_da_semana_sem_feira = dia_da_semana.replace('-feira', '').capitalize()
        proximos_dias.append((dia_futuro.strftime("%d/%m/%y"), dia_da_semana_sem_feira))

    context = {
        "horas": horas,
        "profissionais": profissionais,
        "servicos": servicos,
        "proximos_dias": proximos_dias
    }

    return render(request, "index.html", context)


@require_GET
def verificar_disponibilidade(request):
    profissional_id = request.GET.get("profissional_id")
    data = request.GET.get("data")
    horario_id = request.GET.get("horario_id")

    data_formatada = datetime.datetime.strptime(data, "%d/%m/%y").date()
    disponivel = Agendamento.is_horario_disponivel(
        profissional_id, data_formatada, horario_id
    )

    return JsonResponse({"disponivel": disponivel})


def horarios_disponiveis(request):
    profissional_id = request.GET.get('profissional_id')
    data = request.GET.get('data')
    data = datetime.datetime.strptime(data, "%d/%m/%y").date()

    horarios = Horario.objects.all()
    hora_atual = datetime.datetime.now().time()

    if data == datetime.date.today():
        horarios = [hora for hora in horarios if datetime.datetime.strptime(hora.horario.replace("h", ":"), "%H:%M").time() > hora_atual]

    return JsonResponse({"horarios": [{"id": hora.id, "horario": hora.horario} for hora in horarios]})


def agendar(request):
    if request.method == "POST":
        servico_id = request.POST.get("servico_id")
        profissional_id = request.POST.get("profissional_id")
        horario_id = request.POST.get("horario_id")
        data = request.POST.get("data")
        nome_cliente = request.POST.get("nome_cliente")
        telefone_cliente = request.POST.get("telefone_cliente")

        data_formatada = datetime.datetime.strptime(data, "%d/%m/%y").date()

        if Agendamento.is_horario_disponivel(
            profissional_id, data_formatada, horario_id
        ):
            agendamento = Agendamento(
                servico_selecionado_id=servico_id,
                profissional_selecionado_id=profissional_id,
                horario_selecionado_id=horario_id,
                data=data_formatada,
                nome_cliente=nome_cliente,
                telefone_cliente=telefone_cliente,
            )
            agendamento.save()
            return redirect('index')
        else:
            return JsonResponse({"success": False, "message": "Horário indisponível"})

    return JsonResponse({"success": False, "message": "Requisição inválida"})
