from django.urls import path
from .views import *

urlpatterns = [
    # dashboard urls
    path('', dashboard, name='dashboard'),

    # profissional urls
    path('profissionais/', profissionais, name='profissionais'),
    path('adicionar_profissional/', adicionar_profissional, name='adicionar_profissional'),
    path('atualizar_disponibilidade/', atualizar_disponibilidade, name='atualizar_disponibilidade'),
    path('deletar_profissional/<int:id>/', deletar_profissional, name='deletar_profissional'),

    # horarios url
    path('horarios/', horarios, name='horarios')
]