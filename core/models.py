from django.db import models

class Servico(models.Model):
    id = models.AutoField(primary_key=True)
    servico = models.CharField(max_length=255, null=False)
    valor = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.servico

class Profissional(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    id = models.AutoField(primary_key=True)
    servico_selecionado = models.ForeignKey(Servico, on_delete=models.CASCADE)
    profissional_selecionado = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    nome_cliente = models.CharField(max_length=255, null=False)


