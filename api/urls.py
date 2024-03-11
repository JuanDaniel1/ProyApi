from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'Categorias', views.CategoriasViewSet)
router.register(r'Productos', views.ProductosViewSet)
router.register(r'Pedidos', views.PedidosViewSet)
router.register(r'Factura', views.ItemsViewSet)
router.register(r'Operador', views.OperadorViewSet)
router.register(r'Cliente', views.ClienteViewSet)


urlpatterns = [
    path('', include(router.urls))
]