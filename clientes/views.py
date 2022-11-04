from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cliente
from .forms import ClienteForm


class ListaClienteView(ListView):
    model = Cliente
    queryset = Cliente.objects.all().order_by('nome_completo')

    def get_queryset(self):
        queryset = super().get_queryset()
        filtro_nome = self.request.GET.get('nome') or None

        if filtro_nome:
            queryset = queryset.filter(nome_completo__contains=filtro_nome)

        return queryset


class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    success_url = '/clientes/'


class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    success_url = '/clientes/'


class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = '/clientes/'