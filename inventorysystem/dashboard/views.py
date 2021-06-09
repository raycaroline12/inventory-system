from django.shortcuts import render
from inventory.models import Categoria, Fornecedor, Item, Cliente, Movimentacoes

def dashboard(request):
    labelscat = []
    datacat = []
    labelsforn = []
    dataforn = []

    itens = Item.objects.all()
    itemcount = itens.count()
    clientescount = Cliente.objects.all().count()
    fornecedorescount = Fornecedor.objects.all().count()
    categoriascount = Categoria.objects.all().count()

    queryset = Categoria.objects.all()
    for categoria in queryset:
        labelscat.append(categoria.categoria)
        datacat.append(
            Item.objects.filter(item_categoria=categoria).count()
        )
    
    queryforn = Fornecedor.objects.all()
    for fornecedor in queryforn:
        labelsforn.append(fornecedor.fornecedor)
        dataforn.append(
            Item.objects.filter(item_fornecedor=fornecedor).count()
        )
    
    context = {
        "dashboard": "active",
        'labels_cat': labelscat,
        'data_cat': datacat,
        'labels_forn': labelsforn,
        'data_forn': dataforn,
        'itemcount': itemcount,
        'clientescount': clientescount,
        'fornecedorescount': fornecedorescount,
        'categoriascount': categoriascount,
    }

    return render(request, 'dashboard.html', context)