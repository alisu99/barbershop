from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('verificar_disponibilidade/', verificar_disponibilidade, name='verificar_disponibilidade'),
    path('agendar/', agendar, name='agendar'),
    path('horarios_disponiveis/', horarios_disponiveis, name='horarios_disponiveis'),
]