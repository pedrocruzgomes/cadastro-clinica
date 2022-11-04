from django.db import models


class Cliente(models.Model):
    nome_completo = models.CharField(max_length=256)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=14)
    endereco = models.CharField(max_length=256)
    bairro = models.CharField(max_length=256)
    cidade = models.CharField(max_length=256)