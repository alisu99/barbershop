from django.contrib import admin
from .models import *


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ["nome_cliente", "servico_selecionado", "data", "profissional_selecionado", "horario_selecionado", "finalizado"]
