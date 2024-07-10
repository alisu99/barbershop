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


class Agendamento(models.Model):
    id = models.AutoField(primary_key=True)
    servico_selecionado = models.ForeignKey(Servico, on_delete=models.CASCADE)
    profissional_selecionado = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    horario_selecionado = models.ForeignKey(Horario, on_delete=models.CASCADE)
    data = models.DateField("Data", null=False)
    nome_cliente = models.CharField("Cliente", max_length=255, null=False)
    telefone_cliente = models.CharField("telefone", max_length=255, null=False)

    info = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_cliente

    def is_horario_disponivel(profissional_id, data, horario_id):
        return not Agendamento.objects.filter(
            profissional_selecionado_id=profissional_id,
            data=data,
            horario_selecionado_id=horario_id
        ).exists()
