# tickets/views.py 
from django.urls import reverse_lazy 
from django.views.generic import ListView, CreateView, UpdateView, DeleteView 
from .models import Ticket 
 
class TicketListView(ListView): 
    model = Ticket 
    template_name = "ticket_list.html" 
    context_object_name = "tickets" 
    ordering = ["-fecha_creacion"] 
 
class TicketCreateView(CreateView): 
    model = Ticket 
    fields = ["titulo", "email_contacto", "prioridad", "estado", "descripcion"] 
    template_name = "ticket_form.html" 
    success_url = reverse_lazy("ticket_list") 
 
class TicketUpdateView(UpdateView): 
    model = Ticket 
    fields = ["titulo", "email_contacto", "prioridad", "estado", "descripcion"]
    template_name = "ticket_form.html" 
    success_url = reverse_lazy("ticket_list") 
 
class TicketDeleteView(DeleteView): 
    model = Ticket 
    template_name = "ticket_confirm_delete.html" 
    success_url = reverse_lazy("ticket_list")