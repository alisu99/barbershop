# Generated by Django 5.0.6 on 2024-07-16 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='horario_selecionado',
            field=models.CharField(max_length=255, verbose_name='Horario selecionado'),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='profissional_selecionado',
            field=models.CharField(max_length=255, verbose_name='Profissional selecionado'),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='servico_selecionado',
            field=models.CharField(max_length=255, verbose_name='Serviço selecionado'),
        ),
    ]
