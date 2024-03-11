from rest_framework import serializers
from .models import *
from django import forms

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        #fields = [
        #   'nomProducto',
         #   'desProducto',
         #   'canProducto'
        #]
        fields = '__all__'

class ProductosSerializer(serializers.ModelSerializer):

    class Meta:
  
        model = Productos
        #fields = [
        #   'nomProducto',
         #   'desProducto',
         #   'canProducto'
        #]
        fields = '__all__'


     
        


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        #fields = [
        #   'nomProducto',
         #   'desProducto',
         #   'canProducto'
        #]
        fields = '__all__'

class OperadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operador
        #fields = [
        #   'nomProducto',
         #   'desProducto',
         #   'canProducto'
        #]
        fields = '__all__'

class PedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedidos
        #fields = [
        #   'nomProducto',
         #   'desProducto',
         #   'canProducto'
        #]
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    def get_total(self, obj):
        # Calcula la suma de subtotales de los productos asociados
        return sum(producto.subtotalItem for producto in obj.productoItem.all())
    class Meta:
        model = ItemPedidos
        #fields = [
        #   'nomProducto',
         #   'desProducto',
         #   'canProducto'
        #]
        fields = '__all__'
        

 





