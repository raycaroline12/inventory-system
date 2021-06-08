import django_filters
from django.utils.translation import gettext_lazy as _
from django_filters import CharFilter
from .models import *

class FilterItem(django_filters.FilterSet):
    descricao = CharFilter(
        field_name='descricao',
        lookup_expr='icontains',
        label='Descrição')
    class Meta:
        model = Item
        fields = ['descricao', 'item_categoria', 'item_fornecedor', 'item_filial']
        labels = {
            'descricao': _('Descrição'),
            'item_categoria': _('Categoria'),
            'item_fornecedor': _('Fornecedor'),
            'item_filial': _('Filial'),
        }

class FilterCPF(django_filters.FilterSet):
    descricao = CharFilter(
        field_name='cpf',
        lookup_expr='icontains',
        label='Filtrar por CPF:')
    class Meta:
        fields = ['cpf']
