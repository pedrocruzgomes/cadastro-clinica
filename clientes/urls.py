from django.urls import path
from .views import ListaClienteView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView


urlpatterns = [
    path('', ListaClienteView.as_view(), name='cliente.index'),
    path('cadastrar/', ClienteCreateView.as_view(), name='cliente.novo'),
    path('atualizar/<int:pk>', ClienteUpdateView.as_view(), name='cliente.atualizar'),
    path('excluir/<int:pk>', ClienteDeleteView.as_view(), name='cliente.excluir')
]