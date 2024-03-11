# Generated by Django 4.2.7 on 2023-11-30 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCategoria', models.CharField(max_length=30, verbose_name='Nombre Categoria')),
                ('descripcionCategoria', models.CharField(max_length=30, verbose_name='Descripcion')),
                ('estCategoria', models.BooleanField(default=True, verbose_name='Estado Activo')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCliente', models.CharField(max_length=30, verbose_name='Nombre')),
                ('documentoCliente', models.PositiveBigIntegerField(default=True, verbose_name='Documento')),
                ('emailCliente', models.EmailField(default=True, max_length=254, verbose_name='Email')),
                ('numeroCliente', models.PositiveBigIntegerField(default=True, verbose_name='Telefono')),
            ],
        ),
        migrations.CreateModel(
            name='Operador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreOperador', models.CharField(max_length=30, verbose_name='Nombre')),
                ('emailOperador', models.EmailField(default=True, max_length=30, verbose_name='Email')),
                ('nitOperador', models.PositiveBigIntegerField(default=True, verbose_name='NIT')),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomProducto', models.CharField(max_length=50, verbose_name='Nombre')),
                ('cantProducto', models.PositiveBigIntegerField(default=True, verbose_name='Cantidad')),
                ('precioProducto', models.PositiveBigIntegerField(default=True, verbose_name='Precio Unitario')),
                ('subtotalItem', models.PositiveIntegerField(default=True, editable=False, verbose_name='Subtotal')),
                ('estProducto', models.BooleanField(default=True, verbose_name='Estado Activo')),
                ('catProducto', models.ManyToManyField(to='api.categorias', verbose_name='Categorias')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['nomProducto'],
            },
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numPedido', models.PositiveBigIntegerField(default=True, verbose_name='Numero')),
                ('fechaPedido', models.DateTimeField(verbose_name='Fecha Publicacion')),
                ('clientePedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cliente', verbose_name='Cliente')),
                ('operadorPedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.operador', verbose_name='Operador')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
                'ordering': ['clientePedido'],
            },
        ),
        migrations.CreateModel(
            name='ItemPedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalItem', models.PositiveIntegerField(default=True, editable=False, verbose_name='Total')),
                ('pedidoItem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.pedidos', verbose_name='Pedido')),
                ('productoItem', models.ManyToManyField(null=True, to='api.productos', verbose_name='Productos')),
            ],
        ),
    ]