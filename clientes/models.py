from django.db import models


class Cliente(models.Model):
    nome_completo = models.CharField(max_length=256, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    telefone = models.CharField(max_length=14, null=False, blank=False)
    endereco = models.CharField(max_length=256, null=False, blank=False)
    bairro = models.CharField(max_length=256, null=False, blank=False)
    cidade = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self) -> str:
        return self.nome_completo