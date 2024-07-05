from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import datetime

def index(request):
    servicos = Servico.objects.all()
    profissionais = Profissional.objects.all()
    horas = Horario.objects.all()
    proximos_dias = []
    data_atual = datetime.date.today()

    for i in range(12):
        dia_futuro = data_atual + datetime.timedelta(days=i)
        proximos_dias.append(dia_futuro.strftime("%d/%m"))

    context = {
        'horas': horas,
        'profissionais': profissionais,
        "servicos": servicos,
        "proximos_dias": proximos_dias,
    }

    return render(request, "index.html", context)

