# Generated by Django 5.0.6 on 2024-07-17 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_delete_agendamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('servico_selecionado', models.CharField(max_length=255, verbose_name='Nome do Serviço')),
                ('profissional_selecionado', models.CharField(max_length=255, verbose_name='Nome do Profissional')),
                ('horario_selecionado', models.CharField(max_length=255, verbose_name='Horário')),
                ('data', models.DateField(verbose_name='Data')),
                ('nome_cliente', models.CharField(max_length=255, verbose_name='Cliente')),
                ('telefone_cliente', models.CharField(max_length=255, verbose_name='Telefone')),
                ('finalizado', models.BooleanField(default=False)),
            ],
        ),
    ]
