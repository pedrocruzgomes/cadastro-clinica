from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    nome_completo = models.CharField(max_length=256, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    telefone = models.CharField(max_length=14, null=False, blank=False)
    rua = models.CharField(max_length=256, null=False, blank=False)
    bairro = models.CharField(max_length=256, null=False, blank=False)
    cidade = models.CharField(max_length=256, null=False, blank=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.nome_completo


class Animal(models.Model):
    tipo_animal = models.CharField(max_length=256, null=False, blank=False)
    nome = models.CharField(max_length=256, null=False, blank=False)
    raca = models.CharField(max_length=256, null=True, blank=True)
    nascimento = models.DateField(null=True)
    nome_dono = models.CharField(max_length=256, null=False, blank=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self) -> str:
        return self.nome