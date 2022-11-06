from django.http import HttpResponse, Http404
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cliente, Animal
from .forms import ClienteForm, AnimalForm


class ListaClienteView(ListView):
    model = Cliente
    queryset = Cliente.objects.all().order_by('nome_completo')

    def get_queryset(self):
        queryset = super().get_queryset()
        filtro_nome_cpf = self.request.GET.get('nome' or 'cpf') or None

        if filtro_nome_cpf:
            queryset = queryset.filter(nome_completo__contains=filtro_nome_cpf) or queryset.filter(cpf__contains=filtro_nome_cpf)

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


def animais(request, pk_cliente):
    animais = Animal.objects.filter(nome_dono=pk_cliente)
    return render(request, 'animais/animal_list.html', {'animais': animais, 'pk_cliente': pk_cliente})


def animal_novo(request, pk_cliente):
    form = AnimalForm()
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.cliente_id = pk_cliente;
            animal.save()
            return redirect(reverse('cliente.animais', args=[pk_cliente]))

    return render(request, 'animais/animal_form.html', {'form': form})


def animal_editar(request, pk_cliente, pk):
    animal = get_object_or_404(Animal, pk=pk)
    form = AnimalForm(instance=animal)
    if request.method == "POST":
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect(reverse('cliente.animais', args=[pk_cliente]))

    return render(request, 'animais/animal_form.html', {'form': form})


def animal_remover(request, pk_cliente, pk):
    animal = get_object_or_404(Animal, pk=pk)
    animal.delete()
    return redirect(reverse('cliente.animais', args=[pk_cliente]))