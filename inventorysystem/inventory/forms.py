from django.forms import ModelForm
from django import forms
from .models import Cliente, Item, Categoria, Filial, Fornecedor, Movimentacoes
from django.utils.translation import gettext_lazy as _

class AddItem(ModelForm):
    class Meta:
        model = Item
        fields = ['descricao', 'item_categoria', 'item_fornecedor', 'item_filial']
        labels = {
            'descricao': _('Descrição'),
            'item_categoria': _('Categoria'),
            'item_fornecedor': _('Fornecedor'),
            'item_filial': _('Filial'),
        }

class AddCategoria(ModelForm):
    class Meta:
        model = Categoria
        fields = ['categoria']

class AddFilial(ModelForm):
    class Meta:
        model = Filial
        fields = ['filial']

class AddFornecedor(ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['fornecedor']

class RegisterTransaction(forms.ModelForm):
    class Meta:
        model = Movimentacoes
        fields = ['id_item', 'cpf_cliente']

class RegisterCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        labels = {
            'cpf': _('CPF:'),
            'endereco': _('Endereço'),
            'cep': _('CEP'),
        }