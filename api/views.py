from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializer import *
from rest_framework.response import Response

# Create your views here.
class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer





class PedidosViewSet(viewsets.ModelViewSet):
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializer



class ItemsViewSet(viewsets.ModelViewSet):
    queryset = ItemPedidos.objects.all()
    serializer_class = ItemSerializer



class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class OperadorViewSet(viewsets.ModelViewSet):
    queryset = Operador.objects.all()
    serializer_class = OperadorSerializer

