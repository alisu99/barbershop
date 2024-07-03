from django.db import models

class Servico(models.Model):
    id = models.AutoField(primary_key=True)
    servico = models.CharField('Serviço', max_length=255, null=False)
    valor = models.CharField('Valor', max_length=255, null=False)

    def __str__(self):
        return self.servico

class Profissional(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Nome', max_length=255, null=False)

    def __str__(self):
        return self.nome
    
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Nome', max_length=255, null=False)
    username = models.CharField('Nome de Usuário', max_length=255, null=False, unique=True)
    email = models.EmailField('Email', max_length=100, null=False)
    endereco = models.CharField('Endereço', max_length=1000, null=False)
    bairro = models.CharField('Bairro', max_length=255, null=False)
    cidade = models.CharField('Cidade', max_length=255, null=False)
    uf = models.CharField('UF', max_length=255, null=False)


class Agendamento(models.Model):
    id = models.AutoField(primary_key=True)
    servico_selecionado = models.ForeignKey(Servico, on_delete=models.CASCADE)
    profissional_selecionado = models.ForeignKey( Profissional, on_delete=models.CASCADE)
    nome_cliente = models.CharField('Cliente', max_length=255, null=False)
    telefone_cliente = models.CharField('telefone', max_length=255, null=False)
    email_cliente = models.EmailField('Email', max_length=100)

    def __str__(self):
        return self.nome_cliente