from django.shortcuts import render
from core.models import *

def dashboard(request):
    agendamentos = Agendamento.objects.all()
    context = {
        'agendamentos': agendamentos
    }

    return render(request, 'dashboard.html', context)
