from import_export import resources
from import_export.fields import Field
from .models import Cliente

class ClienteResource(resources.ModelResource):
    nome_completo = Field(attribute='nome_completo', column_name='Nome Cliente')
    cpf = Field(attribute='cpf', column_name='CPF')
    data_nascimento = Field(attribute='data_nascimento', column_name='Data de Nascimento')
    telefone = Field(attribute='telefone', column_name='Telefone')
    rua = Field(attribute='rua', column_name='Rua')
    bairro = Field(attribute='bairro', column_name='Bairro')
    cidade = Field(attribute='cidade', column_name='Cidade')
    class Meta:
        model = Cliente
        fields = ['nome_completo', 'cpf', 'data_nascimento', 'telefone', 'rua', 'bairro', 'cidade']