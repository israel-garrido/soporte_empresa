# tickets/admin.py 
from django.contrib import admin 
from .models import Ticket 
 
@admin.register(Ticket) 
class TicketAdmin(admin.ModelAdmin): 
    list_display = ("id", "titulo", "prioridad", "estado", "email_contacto", "fecha_creacion") 
    list_filter = ("prioridad", "estado") 
    search_fields = ("titulo", "email_contacto")