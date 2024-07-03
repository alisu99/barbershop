from django.contrib import admin
from .models import Profissional, Agendamento, Servico, Usuario


@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ["nome"]


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ["nome_cliente", "servico_selecionado", "profissional_selecionado"]


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ["servico", "valor"]

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["nome", "username", "email"]