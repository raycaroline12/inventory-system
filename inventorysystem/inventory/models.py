from datetime import MAXYEAR
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone


class Categoria(models.Model):
    categoria = models.CharField(max_length=200)
    def __str__(self):
        return self.categoria

class Fornecedor(models.Model):
    fornecedor = models.CharField(max_length=200)
    def __str__(self):
        return self.fornecedor

class Filial(models.Model):
    filial = models.CharField(max_length=200)
    def __str__(self):
        return self.filial

class Item(models.Model):
    descricao = models.CharField(max_length=200)
    data_cadastro = models.DateTimeField(default=timezone.now)
    quantidade = models.IntegerField()
    item_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    item_fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, null=True)
    item_filial = models.ForeignKey(Filial, on_delete=models.CASCADE, null=True)

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=11)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    numero = models.CharField(max_length=5)
    cep = models.CharField(max_length=8)
