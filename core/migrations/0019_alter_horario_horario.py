# Generated by Django 5.0.6 on 2024-07-10 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_remove_usuario_bairro_remove_usuario_cidade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='horario',
            field=models.TimeField(max_length=10, unique=True),
        ),
    ]
