from django.db import models


class Agendamento(models.Model):
    id = models.AutoField(primary_key=True)
    servico_selecionado = models.CharField(
        "Nome do Serviço", max_length=255, null=False
    )
    profissional_selecionado = models.CharField(
        "Nome do Profissional", max_length=255, null=False
    )
    horario_selecionado = models.CharField("Horário", max_length=255, null=False)
    data = models.DateField("Data", null=False)
    nome_cliente = models.CharField("Cliente", max_length=255, null=False)
    telefone_cliente = models.CharField("Telefone", max_length=255, null=False)
    finalizado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_cliente

    @staticmethod
    def is_horario_disponivel(profissional_nome, data, horario):
        return not Agendamento.objects.filter(
            profissional_selecionado=profissional_nome,
            data=data,
            horario_selecionado=horario,
        ).exists()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Sobrescrevendo o método de exclusão para evitar a exclusão em cascata
        super().delete(*args, **kwargs)
        # Aqui você pode adicionar qualquer lógica adicional após a exclusão do agendamento
