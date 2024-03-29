"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('addCliente', include('app.urls')),
    path('agregarCliente', include('app.urls')),
    path('listar_clientes', include('app.urls')),
    path('editar_cliente/<int:cliente_id>', include('app.urls')),
    path('borrar_cliente/<int:cliente_id>', include('app.urls')),
    path('inicio', include('app.urls')),
    path('Tienda', include('app.urls')),
    path('Quienes_somos', include('app.urls')),
]

