from datetime import MAXYEAR
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField
from django.utils import timezone
from django.contrib.auth.models import User
from cpf_field.models import CPFField


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
    item_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    item_fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    item_filial = models.ForeignKey(Filial, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.descricao

class Cliente(models.Model):
    cpf = CPFField(primary_key=True)
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=11)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    numero = models.CharField(max_length=5)
    cep = models.CharField(max_length=8)
    
    def __str__(self):
        return self.nome

class Movimentacoes(models.Model):
    id_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    cpf_cliente = models.ForeignKey(Cliente, on_delete=CASCADE)
    data_saida = models.DateTimeField(default=timezone.now)
    quantidade = IntegerField(default=0)