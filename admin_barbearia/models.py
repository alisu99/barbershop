from django.db import models


class Servico(models.Model):
    id = models.AutoField(primary_key=True)
    servico = models.CharField("Serviço", max_length=255, null=False)
    valor = models.CharField("Valor", max_length=255, null=False)

    def __str__(self):
        return self.servico


class Profissional(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField("Nome", max_length=255, null=False)
    disponivel = models.BooleanField("Disponível", default=True)

    def __str__(self):
        return self.nome


class Horario(models.Model):
    id = models.AutoField(primary_key=True)
    horario = models.CharField(max_length=10, null=False, unique=True)

    def __str__(self):
        return self.horario


class Barbearia(models.Model):
    nome = models.CharField("Nome", max_length=255, null=False)
    telefone = models.CharField("Telefone", max_length=255, null=False)
    localizacao = models.CharField("Localização", max_length=500, null=False)

    def __str(self):
        return self.nome


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField("Nome", max_length=255, null=False)
    username = models.CharField(
        "Nome de Usuário", max_length=255, null=False, unique=True
    )
    email = models.EmailField("Email", max_length=100, null=False)
    telefone = models.CharField("Telefone", max_length=15, null=False)
