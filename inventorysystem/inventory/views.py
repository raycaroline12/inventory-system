from django.shortcuts import get_object_or_404, render, redirect
from inventory.models import Categoria, Fornecedor, Filial, Item, Cliente, Movimentacoes
from django.contrib.auth.decorators import login_required
from .forms import AddItem, AddFornecedor, AddCategoria, AddFilial, RegisterCliente, RegisterTransaction
from .filters import FilterItem, FilterCPF
from django.views.generic.edit import CreateView

@login_required
def inventory(request):
    itens = Item.objects.all()
    categorias = Categoria.objects.all()
    fornecedores = Fornecedor.objects.all()
    filiais = Filial.objects.all()

    myFilter = FilterItem(request.GET, queryset=itens)
    itens = myFilter.qs

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
        "filial_form": filial_form,
        "myFilter": myFilter,
    }

    return render(request, 'tables.html', context)

@login_required
def editItem(request, my_id):
     itens = Item.objects.all()
     
     itemToEdit = Item.objects.get(id=my_id)
     edit_form = AddItem(request.POST or None, instance=itemToEdit)


     if request.method == 'POST' and 'delete_item' in request.POST:
          item = get_object_or_404(Item, id=my_id)
          item.delete()
          return redirect('inventory')
     elif request.method == 'POST' and 'edit_item' in request.POST:
          if edit_form.is_valid():
               edit_form.save()
               return redirect('inventory')
     context = {
          "item": itens,
          "edit_form": edit_form
     }

     return render(request, 'edit_item.html', context)


@login_required
def transactions(request):
     movimentacoes = Movimentacoes.objects.all()
     context = {
           "transactions": "active",
           "movimentacoes": movimentacoes,
     }
     return render(request, 'transactions.html', context)

@login_required
def register_transaction(request):
     itens = Item.objects.all()
     clientes = Cliente.objects.all()

     cpfFilter = FilterCPF(request.GET, queryset=clientes)
     clientes = cpfFilter.qs   

     if request.method == "POST":
         transaction_form = RegisterTransaction(request.POST)
         if transaction_form.is_valid():
              transaction_form.instance.created_by = request.user
              transaction_form.save()
              return redirect('transactions')
     else:
         transaction_form = RegisterTransaction()
     
     if request.method == "POST":
         client_form = RegisterCliente(request.POST)
         if client_form.is_valid():
            client_form.save()
            
            return redirect('register_transaction')
     else:
         client_form = RegisterCliente()

     context = {
          "transactions": "active",
          "transaction_form": transaction_form,
          "itens": itens,
          "clientes": clientes,
          "client_form": client_form,
          "cpfFilter": cpfFilter,
     }

     return render(request, 'register_transaction.html', context)