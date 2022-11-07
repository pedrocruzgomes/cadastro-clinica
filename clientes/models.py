from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    nome_completo = models.CharField(max_length=256, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    telefone = models.CharField(max_length=14, null=False, blank=False)
    endereco = models.CharField(max_length=256, null=False, blank=False)
    bairro = models.CharField(max_length=256, null=False, blank=False)
    cidade = models.CharField(max_length=256, null=False, blank=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.nome_completo


class Animal(models.Model):
    nome = models.CharField(max_length=256, null=False, blank=False)
    raca = models.CharField(max_length=256, null=False, blank=False)
    nascimento = models.DateField(null = False, blank=False)
    nome_dono = models.CharField(max_length=256, null=False, blank=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome