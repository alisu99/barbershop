from django.shortcuts import render
from .models import Profissional, Servico, Agendamento
import datetime


def index(request):
    servico = Servico.objects.all()
    profissional = Profissional.objects.all()
    data_atual = datetime.date.today()
    proximos_dias = []

    for i in range(12):
        dia_futuro = data_atual + datetime.timedelta(days=i)
        proximos_dias.append(dia_futuro.strftime("%d/%m"))

    context = {
        "servicos": servico,
        "profissionais": profissional,
        "data_atual": data_atual.strftime("%d/%m/%Y"),
        "proximos_dias": proximos_dias,
    }

    return render(request, "index.html", context)
