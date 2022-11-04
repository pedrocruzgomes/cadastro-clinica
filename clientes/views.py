from django.shortcuts import render
from django.views.generic import ListView
from .models import Cliente


class ListaClienteView(ListView):
    model = Cliente
    queryset = Cliente.objects.all().order_by('nome_completo')