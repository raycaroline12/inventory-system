import django_filters
from django.utils.translation import gettext_lazy as _
from django_filters import CharFilter
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field
from crispy_forms.bootstrap import *
from .models import *

class FilterItem(django_filters.FilterSet):
    descricao = CharFilter(
        field_name='descricao',
        lookup_expr='icontains',
        label='Descrição')
    
    helper = FormHelper()
    helper.form_class = 'form-inline'
    helper.layout = Layout(
        Div(
            Field('descricao', wrapper_class='col-md-3'),
            Field('item_categoria', wrapper_class='col-md-3'),
            Field('item_fornecedor', wrapper_class='col-md-3'),
            Field('item_filial', wrapper_class='col-md-3'),
        css_class='row') 
    )

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
    cpf = CharFilter(
        field_name='cpf',
        lookup_expr='icontains',
        label='Filtrar por CPF:')
    class Meta:
        model = Cliente
        fields = ['cpf']
