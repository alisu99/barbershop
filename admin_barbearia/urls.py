from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('finalizar/<int:id>', finalizar, name='finalizar'),
    path('adm/', adm, name='adm'),
    path('profissionais/', profissionais, name='profissionais'),
    path('atualizar-disponibilidade/', atualizar_disponibilidade, name='atualizar_disponibilidade'),
    path('adicionar-profissional/', adicionar_profissional, name='adicionar_profissional')
]
