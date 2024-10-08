# Generated by Django 5.0.6 on 2024-07-16 22:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_delete_agendamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome_servico', models.CharField(max_length=255, verbose_name='Nome do Serviço')),
                ('nome_profissional', models.CharField(max_length=255, verbose_name='Nome do Profissional')),
                ('horario', models.CharField(max_length=255, verbose_name='Horário')),
                ('data', models.DateField(verbose_name='Data')),
                ('nome_cliente', models.CharField(max_length=255, verbose_name='Cliente')),
                ('telefone_cliente', models.CharField(max_length=255, verbose_name='Telefone')),
                ('finalizado', models.BooleanField(default=False)),
                ('horario_selecionado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.horario')),
                ('profissional_selecionado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.profissional')),
                ('servico_selecionado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.servico')),
            ],
        ),
    ]
