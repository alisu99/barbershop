from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('verificar_profissionais/', verificar_profissionais, name='verificar_profissionais'),
    path('verificar_horarios/', verificar_horarios, name='verificar_horarios'),
    path('agendar/', agendar, name='agendar'),
]