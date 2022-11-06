from django import forms
from .models import Cliente, Animal


class ClienteForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.TextInput(
            attrs={"type": "date"}
        )
    )
    class Meta:
        model = Cliente
        fields = ['nome_completo', 'cpf', 'telefone', 'endereco', 'bairro', 'cidade', 'data_nascimento']


class AnimalForm(forms.ModelForm):
    nascimento = forms.DateField(
        widget=forms.TextInput(
            attrs={"type": "date"}
        )
    )
    class Meta:
        model = Animal
        fields = ['nome', 'raca', 'nascimento', 'nome_dono']