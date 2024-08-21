from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from core.models import *
from .models import *
import datetime


def dashboard(request):
    agendamentos = Agendamento.objects.filter(finalizado=False).order_by("-data")
    historicos = Agendamento.objects.filter(finalizado=True).order_by("-data")
    total_agendamentos_hoje = len(
        Agendamento.objects.filter(data=datetime.date.today())
    )
    agendamentos_abertos_hoje = len(
        Agendamento.objects.filter(finalizado=False, data=datetime.date.today())
    )
    agendamentos_fechados_hoje = len(
        Agendamento.objects.filter(finalizado=True, data=datetime.date.today())
    )
    context = {
        "agendamentos": agendamentos,
        "historicos": historicos,
        "total_agendamentos_hoje": total_agendamentos_hoje,
        "agendamentos_abertos_hoje": agendamentos_abertos_hoje,
        "agendamentos_fechados_hoje": agendamentos_fechados_hoje,
    }
    return render(request, "dashboard.html", context)


def finalizar(request, id):
    agendamento = Agendamento.objects.filter(id=id).first()
    agendamento.finalizado = True
    agendamento.save()
    return redirect(dashboard)


def profissionais(request):
    profissionais = Profissional.objects.all()
    context = {
        "profissionais": profissionais,
    }
    return render(request, "profissionais.html", context)


def adicionar_profissional(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        profissional = Profissional(nome=nome)
        profissional.save()
    return redirect("profissionais")


@csrf_exempt
@require_POST
def atualizar_disponibilidade(request):
    profissional_id = request.POST.get("id")
    disponibilidade = request.POST.get("disponibilidade") == "true"

    profissional = Profissional.objects.filter(id=profissional_id).first()
    if profissional:
        profissional.disponivel = disponibilidade
        profissional.save()
        return JsonResponse({"status": "success"})
    return JsonResponse(
        {"status": "error", "message": "Profissional não encontrado"}, status=404
    )


def deletar_profissional(request, id):
    profissional = get_object_or_404(Profissional, id=id)
    profissional.delete()
    return redirect("profissionais")


def horarios(request):
    return render(request, 'horarios.html')