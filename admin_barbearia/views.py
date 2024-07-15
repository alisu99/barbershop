from django.shortcuts import render, redirect
from core.models import *

def dashboard(request):
    agendamentos = Agendamento.objects.filter(finalizado=False).order_by('data')
    historicos = Agendamento.objects.filter(finalizado=True).order_by('-data')
    context = {
        'agendamentos': agendamentos,
        'historicos': historicos,
    }

    return render(request, 'dashboard.html', context)

def finalizar(request, id):
    agendamento = Agendamento.objects.filter(id=id).first()
    agendamento.finalizado = True
    agendamento.save()
    return redirect(dashboard)