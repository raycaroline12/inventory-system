# Generated by Django 3.1.7 on 2021-06-06 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cpf', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=11)),
                ('cidade', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=200)),
                ('numero', models.CharField(max_length=5)),
                ('cep', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Filial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filial', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fornecedor', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
                ('data_cadastro', models.DateTimeField(default=django.utils.timezone.now)),
                ('quantidade', models.IntegerField()),
                ('item_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.categoria')),
                ('item_filial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.filial')),
                ('item_fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.fornecedor')),
            ],
        ),
        migrations.CreateModel(
            name='Movimentacoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_saida', models.DateTimeField(default=django.utils.timezone.now)),
                ('cpf_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.cliente')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.item')),
            ],
        ),
    ]
