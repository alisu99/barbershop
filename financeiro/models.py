from django.db import models
from django.conf import settings
from admin_barbearia.models import Usuario

class Credito(models.Model):
    usuario = models.OneToOneField(
        Usuario, on_delete=models.CASCADE, related_name='credito'
    )
    saldo = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )

    def __str__(self):
        return f"Crédito de {self.usuario.nome}: R${self.saldo:.2f}"


class Transacao(models.Model):
    TIPOS_DE_TRANSACAO = [
        ('recarga', 'Recarga'),
        ('compra', 'Compra'),
    ]

    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name='transacoes'
    )
    tipo = models.CharField(
        max_length=10, choices=TIPOS_DE_TRANSACAO, default='recarga'
    )
    valor = models.DecimalField(
        max_digits=10, decimal_places=2
    )
    data = models.DateTimeField(auto_now_add=True)
    metodo = models.CharField(
        max_length=50, choices=[('pix', 'Pix'), ('cartao', 'Cartão de Crédito')]
    )

    def __str__(self):
        return f"{self.tipo.capitalize()} - {self.valor} - {self.data.strftime('%d/%m/%Y %H:%M')}"
