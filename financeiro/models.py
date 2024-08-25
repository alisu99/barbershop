from django.db import models
from django.conf import settings

class Credito(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.usuario} - {self.valor}'

class Pagamento(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    id_transacao = models.CharField(max_length=255, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario} - {self.valor} - {self.id_transacao}'
