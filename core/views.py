from django.shortcuts import render
from .models import Profissional, Servico, Agendamento

def index(request):
    servico = Servico.objects.all()
    profissional = Profissional.objects.all()
    
    context = {
        'servicos': servico,
        'profissionais': profissional,
    }
    
    return render(request, 'index.html', context)