from django.shortcuts import render
from inventory.models import Categoria, Fornecedor, Filial, Item, Cliente


def inventory(request):
    itens = Item.objects.all()
    categorias = Categoria.objects.all()
    fornecedores = Fornecedor.objects.all()
    filiais = Filial.objects.all()
    clientes = Cliente.objects.all()

    context = {
        "inventory": "active",
        "itens": itens,
        "categorias": categorias,
        "fornecedores": fornecedores,
        "filiais": filiais,
    }

    return render(request, 'tables.html', context)
