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
# tickets/urls.py 
from django.urls import path 
from .views import TicketListView, TicketCreateView, TicketUpdateView, TicketDeleteView 
 
urlpatterns = [ 
    path("", TicketListView.as_view(), name="ticket_list"), 
    path("nuevo/", TicketCreateView.as_view(), name="ticket_create"), 
    path("editar/<int:pk>/", TicketUpdateView.as_view(), name="ticket_update"), 
    path("eliminar/<int:pk>/", TicketDeleteView.as_view(), name="ticket_delete"), 
]