"""
URL configuration for soporte_empresa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from django.views.generic import TemplateView # Importamos TemplateView

# --- PERSONALIZACIÓN DEL ADMIN DE DJANGO ---
# Cambia el texto de la barra superior
admin.site.site_header = "Administración Soporte Empresa"

# Cambia el texto que aparece en la pestaña del navegador
admin.site.site_title = "Admin Soporte Empresa"

# Cambia el subtítulo en la página principal del admin
admin.site.index_title = "Panel de Control Principal"
# -------------------------------------------

urlpatterns = [
    path('admin/', admin.site.urls),
    path("tickets/", include("tickets.urls")),
    path("biblioteca/", include("biblioteca.urls")),
    
    # Configuramos la ruta raíz para que muestre nuestro index central
    path('', TemplateView.as_view(template_name='index.html'), name='index'),

    path('cuentas/', include('django.contrib.auth.urls')), 
    path('inventario/', include('inventario.urls')), 
]
