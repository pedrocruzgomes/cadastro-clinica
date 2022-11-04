from django.urls import path
from .views import ListaClienteView


urlpatterns = [
    path('', ListaClienteView.as_view(), name='cliente.index')
]