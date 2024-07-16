from django.contrib import admin
from .models import *


@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ["nome"]


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ["nome_cliente", "servico_selecionado", "data", "profissional_selecionado", "horario_selecionado", "finalizado"]


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ["servico", "valor"]

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["nome", "username", "email"]


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ["horario"]
