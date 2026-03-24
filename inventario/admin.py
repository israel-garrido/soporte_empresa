from django.contrib import admin

# Register your models here.
from .models import Notebook 
 
 
@admin.register(Notebook) 
class NotebookAdmin(admin.ModelAdmin): 
    list_display = ('codigo', 'marca', 'modelo', 'estado', 'disponible') 
    search_fields = ('codigo', 'marca', 'modelo') 
    list_filter = ('estado', 'disponible')