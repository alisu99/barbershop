# Generated by Django 5.0.6 on 2024-07-03 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='Nome de Usuário')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('endereco', models.CharField(max_length=1000, verbose_name='Endereço')),
                ('bairro', models.CharField(max_length=255, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=255, verbose_name='Cidade')),
                ('uf', models.CharField(max_length=255, verbose_name='UF')),
            ],
        ),
        migrations.AlterField(
            model_name='profissional',
            name='nome',
            field=models.CharField(max_length=255, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='servico',
            field=models.CharField(max_length=255, verbose_name='Serviço'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='valor',
            field=models.CharField(max_length=255, verbose_name='Valor'),
        ),
        migrations.DeleteModel(
            name='Agendamento',
        ),
    ]
