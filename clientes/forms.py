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
        fields = ['nome_completo', 'cpf', 'data_nascimento', 'telefone', 'rua', 'bairro', 'cidade']


class AnimalForm(forms.ModelForm):
    nascimento = forms.DateField(
        widget=forms.TextInput(
            attrs={"type": "date"}
        )
    )
    image = forms.ImageField(label='Imagem', required=False)
    class Meta:
        model = Animal
        fields = ['tipo_animal', 'nome', 'raca', 'nascimento', 'nome_dono', 'image']