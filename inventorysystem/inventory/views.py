from django.shortcuts import render, redirect
from inventory.models import Categoria, Fornecedor, Filial, Item, Cliente
from django.contrib.auth.decorators import login_required
from .forms import AddItem, AddFornecedor, AddCategoria, AddFilial

@login_required
def inventory(request):
    itens = Item.objects.all()
    categorias = Categoria.objects.all()
    fornecedores = Fornecedor.objects.all()
    filiais = Filial.objects.all()

    if request.method == "POST":
         item_form = AddItem(request.POST)
         if item_form.is_valid():
            item_form.save()
            
            return redirect('inventory')
    else:
         item_form = AddItem()

    if request.method == "POST":
         categoria_form = AddCategoria(request.POST)
         if categoria_form.is_valid():
            categoria_form.save()
            
            return redirect('inventory')
    else:
         categoria_form = AddCategoria()

    if request.method == "POST":
         fornecedor_form = AddFornecedor(request.POST)
         if fornecedor_form.is_valid():
            fornecedor_form.save()
            
            return redirect('inventory')
    else:
         fornecedor_form = AddFornecedor()

    if request.method == "POST":
         filial_form = AddFilial(request.POST)
         if filial_form.is_valid():
            filial_form.save()
            
            return redirect('inventory')
    else:
         filial_form = AddFilial()

    context = {
        "inventory": "active",
        "itens": itens,
        "categorias": categorias,
        "fornecedores": fornecedores,
        "filiais": filiais,
        "item_form": item_form,
        "categoria_form": categoria_form,
        "fornecedor_form": fornecedor_form,
        "filial_form": filial_form
    }

    return render(request, 'tables.html', context)
