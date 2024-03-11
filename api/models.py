from django.db import models
   
class Categorias(models.Model):
    nombreCategoria = models.CharField(max_length=30, verbose_name='Nombre Categoria')
    descripcionCategoria = models.CharField(max_length=30, verbose_name="Descripcion")
    estCategoria = models.BooleanField(default=True, verbose_name='Estado Activo')


    def __str__(self):
        return self.nombreCategoria
    
class Productos(models.Model):
    nomProducto = models.CharField(max_length=50, verbose_name='Nombre')
    catProducto = models.ManyToManyField(Categorias, verbose_name="Categorias")
    cantProducto = models.PositiveBigIntegerField(default=True, verbose_name="Cantidad")
    precioProducto = models.PositiveBigIntegerField(default=True, verbose_name="Precio Unitario")
    subtotalItem = models.PositiveIntegerField(default=True, verbose_name="Subtotal", editable=False)
    estProducto = models.BooleanField(default=True, verbose_name='Estado Activo')

    def calcular_subtotal(self):
        self.subtotalItem = self.cantProducto * self.precioProducto

    
    def save(self, *args, **kwargs):
        # Calcula el subtotal antes de guardar el objeto
        self.calcular_subtotal()
        # Llama al método save del modelo para guardar el objeto
        super().save(*args, **kwargs)




    def __str__(self):
        return self.nomProducto
    
   

    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'
        ordering=['nomProducto']

     

    
class Cliente(models.Model):
    nombreCliente = models.CharField(max_length=30, verbose_name="Nombre")
    documentoCliente = models.PositiveBigIntegerField(default=True, verbose_name="Documento")
    emailCliente = models.EmailField(default=True, verbose_name="Email")
    numeroCliente = models.PositiveBigIntegerField(default=True, verbose_name="Telefono")

    def __str__(self):
        return self.nombreCliente

class Operador(models.Model):
    nombreOperador = models.CharField(max_length=30, verbose_name="Nombre")
    emailOperador = models.EmailField(default=True, max_length=30, verbose_name="Email")
    nitOperador = models.PositiveBigIntegerField(default=True, verbose_name="NIT")

    def __str__(self):
        return self.nombreOperador


class Pedidos(models.Model):
    clientePedido = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    operadorPedido = models.ForeignKey(Operador, on_delete=models.CASCADE, verbose_name="Operador")
    numPedido = models.PositiveBigIntegerField(default=True, verbose_name='Numero')
    fechaPedido = models.DateTimeField('Fecha Publicacion')

    def __str__(self):
        return f"{self.numPedido} - {self.clientePedido}"
    class Meta:
        verbose_name='Pedido'
        verbose_name_plural='Pedidos'
        ordering=['clientePedido']


class ItemPedidos(models.Model):
    pedidoItem = models.ForeignKey(Pedidos, null=True, on_delete=models.CASCADE, verbose_name='Pedido')
    productoItem = models.ManyToManyField(Productos, null=True, verbose_name='Productos')
    
    

  

    

        # Llama al método save del objeto principal para guardar la relación ManyToMany con el ID asignado
    

    def __str__(self):
        return f"{self.pedidoItem.numPedido}"
    
    
    
    
    

  

