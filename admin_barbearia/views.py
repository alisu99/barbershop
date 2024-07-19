from django.shortcuts import render, redirect
from core.models import *
import datetime

def dashboard(request):
    agendamentos = Agendamento.objects.filter(finalizado=False).order_by('-data')
    historicos = Agendamento.objects.filter(finalizado=True).order_by('-data')
    total_agendamentos_hoje = len(Agendamento.objects.filter(data=datetime.date.today()))
    agendamentos_abertos_hoje = len(Agendamento.objects.filter(finalizado=False, data=datetime.date.today()))
    agendamentos_fechados_hoje = len(Agendamento.objects.filter(finalizado=True, data=datetime.date.today()))
    context = {
        'agendamentos': agendamentos,
        'historicos': historicos,
        'total_agendamentos_hoje': total_agendamentos_hoje,
        'agendamentos_abertos_hoje': agendamentos_abertos_hoje,
        'agendamentos_fechados_hoje': agendamentos_fechados_hoje,
    }
    return render(request, 'dashboard.html', context)

def finalizar(request, id):
    agendamento = Agendamento.objects.filter(id=id).first()
    agendamento.finalizado = True
    agendamento.save()
    return redirect(dashboard)

def adm(request):
    return render(request, 'administracao.html')