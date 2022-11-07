from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ListaClienteView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView, AnimalDeleteView
from . import views


urlpatterns = [
    path('', login_required(ListaClienteView.as_view()), name='cliente.index'),
    path('cadastrar/', login_required(ClienteCreateView.as_view()), name='cliente.novo'),
    path('<int:pk>/atualizar', login_required(ClienteUpdateView.as_view()), name='cliente.atualizar'),
    path('<int:pk>/excluir', login_required(ClienteDeleteView.as_view()), name='cliente.excluir'),
    path('<int:pk_cliente>/animais', login_required(views.animais), name='cliente.animais'),
    path('<int:pk_cliente>/animal/novo/', login_required(views.animal_novo), name='animal.novo'),
    path('<int:pk_cliente>/animal/<int:pk>/atualizar', login_required(views.animal_editar), name='animal.atualizar'),
    path('<int:pk_cliente>/animal/<int:pk>/excluir', login_required(AnimalDeleteView.as_view()), name='animal.excluir'),

]