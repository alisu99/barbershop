from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profissionais/', profissionais, name='profissionais'),
    path('adicionar_profissional/', adicionar_profissional, name='adicionar_profissional'),
    path('adicionar_servico/', adicionar_servico, name='adicionar_servico'),
    path('atualizar_disponibilidade/', atualizar_disponibilidade, name='atualizar_disponibilidade'),
    path('deletar_profissional/<int:id>/', deletar_profissional, name='deletar_profissional'),
    path('adicionar_horario/', adicionar_horario, name='adicionar_horario'),
    path('remover_horario/<int:id>/', remover_horario, name='remover_horario'),
    path('remover_todos_horarios/', remover_todos_horarios, name='remover_todos_horarios'),
    path('finalizar/<int:id>/', finalizar, name='finalizar'),
]