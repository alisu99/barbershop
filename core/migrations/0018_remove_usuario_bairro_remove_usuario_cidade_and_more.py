# Generated by Django 5.0.6 on 2024-07-10 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_agendamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='bairro',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='cidade',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='endereco',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='uf',
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='info',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
