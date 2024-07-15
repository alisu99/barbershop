from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('finalizar/<int:id>', finalizar, name='finalizar')
]