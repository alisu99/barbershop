from django.contrib import admin
from .models import *


@admin.register(Barbearia)
class BarbeariaAdmin(admin.ModelAdmin):
    list_display = ["nome", "telefone", "localizacao"]


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["nome", "username", "email"]

@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ["nome"]


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ["servico", "valor"]


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ["horario"]
