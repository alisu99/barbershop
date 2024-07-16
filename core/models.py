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

    def __str__(self):
        return self.nome


class Horario(models.Model):
    id = models.AutoField(primary_key=True)
    horario = models.CharField(max_length=10, null=False, unique=True)

    def __str__(self):
        return self.horario


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField("Nome", max_length=255, null=False)
    username = models.CharField(
        "Nome de Usuário", max_length=255, null=False, unique=True
    )
    email = models.EmailField("Email", max_length=100, null=False)
    telefone = models.CharField("Telefone", max_length=15, null=False)


class Agendamento(models.Model):
    id = models.AutoField(primary_key=True)
    servico_selecionado = models.ForeignKey('Servico', on_delete=models.SET_NULL, null=True, blank=True)
    nome_servico = models.CharField("Nome do Serviço", max_length=255, null=False)
    profissional_selecionado = models.ForeignKey('Profissional', on_delete=models.SET_NULL, null=True, blank=True)
    nome_profissional = models.CharField("Nome do Profissional", max_length=255, null=False)
    horario_selecionado = models.ForeignKey('Horario', on_delete=models.SET_NULL, null=True, blank=True)
    horario = models.CharField("Horário", max_length=255, null=False)
    data = models.DateField("Data", null=False)
    nome_cliente = models.CharField("Cliente", max_length=255, null=False)
    telefone_cliente = models.CharField("Telefone", max_length=255, null=False)
    finalizado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_cliente

    @staticmethod
    def is_horario_disponivel(profissional_id, data, horario_id):
        return not Agendamento.objects.filter(
            profissional_selecionado_id=profissional_id,
            data=data,
            horario_selecionado_id=horario_id
        ).exists()
    
    def save(self, *args, **kwargs):
        if self.servico_selecionado:
            self.nome_servico = self.servico_selecionado.servico
        if self.profissional_selecionado:
            self.nome_profissional = self.profissional_selecionado.nome
        if self.horario_selecionado:
            self.horario = self.horario_selecionado.horario
        super().save(*args, **kwargs)
