# Generated by Django 5.0.6 on 2024-07-16 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='Nome de Usuário')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
            ],
        ),
    ]
