from django.urls import path
from .views import ListaClienteView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView
from . import views


urlpatterns = [
    path('', ListaClienteView.as_view(), name='cliente.index'),
    path('cadastrar/', ClienteCreateView.as_view(), name='cliente.novo'),
    path('<int:pk>/atualizar', ClienteUpdateView.as_view(), name='cliente.atualizar'),
    path('<int:pk>/excluir', ClienteDeleteView.as_view(), name='cliente.excluir'),
    path('<int:pk_cliente>/animais', (views.animais), name='cliente.animais'),
    path('<int:pk_cliente>/animal/novo/', (views.animal_novo), name='animal.novo'),
    path('<int:pk_cliente>/animal/<int:pk>/atualizar', (views.animal_editar), name='animal.editar'),
    path('<int:pk_cliente>/animal/<int:pk>/excluir', (views.animal_remover), name='animal.remover'),

]