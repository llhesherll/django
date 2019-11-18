from django.urls import path, include
from . import views

urlpatterns = [

    path('agregar_cliente', views.Cliente_Create.as_view(), name="cliente_crear"),
    path('listar_clientes', views.listar_clientes),
    path('editar_cliente/<int:cliente_id>', views.editar_cliente),
    path('borrar_cliente/<int:cliente_id>', views.borrar_cliente),
    path('', views.index),
    path('inicio', views.index),
    path('Tienda', views.Tienda),
    path('Quienes_somos', views.Quienes_somos),
    
]
