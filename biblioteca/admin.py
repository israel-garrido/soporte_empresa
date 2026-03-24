from django.contrib import admin 
from .models import Socio, Editorial, Categoria, Libro, Prestamo 
 
admin.site.site_header = "Administración Biblioteca Académica" 
admin.site.site_title = "Biblioteca Admin" 
admin.site.index_title = "Panel de Control" 
 
 
class PrestamoInline(admin.TabularInline): 
    model = Prestamo 
    extra = 1 
    autocomplete_fields = ("libro",) 
    
@admin.register(Socio) 
class SocioAdmin(admin.ModelAdmin): 
    list_display = ("id", "rut", "get_username", "get_nombre", "get_email") 
    search_fields = ("rut", "user__username", "user__email", "user__first_name", 
"user__last_name") 
    inlines = [PrestamoInline] 
 
    def get_username(self, obj): 
        return obj.user.username 
    get_username.short_description = "Username" 
 
    def get_nombre(self, obj): 
        return obj.user.get_full_name() 
    get_nombre.short_description = "Nombre" 
 
    def get_email(self, obj): 
        return obj.user.email 
    get_email.short_description = "Email" 
 
@admin.register(Editorial) 
class EditorialAdmin(admin.ModelAdmin): 
    list_display = ("id", "nombre") 
    search_fields = ("nombre",) 
 
 
@admin.register(Categoria) 
class CategoriaAdmin(admin.ModelAdmin): 
    list_display = ("id", "nombre") 
    search_fields = ("nombre",) 
 
 
@admin.register(Libro) 
class LibroAdmin(admin.ModelAdmin): 
    list_display = ("id", "titulo", "isbn", "anio_publicacion", "editorial") 
    list_filter = ("editorial", "categorias") 
    search_fields = ("titulo", "isbn", "editorial__nombre", "categorias__nombre") 
 
    # UX para M2M 
    filter_horizontal = ("categorias",) 
 
@admin.register(Prestamo) 
class PrestamoAdmin(admin.ModelAdmin): 
    list_display = ("id", "socio", "libro", "fecha_prestamo", "fecha_devolucion", 
"estado") 
    list_filter = ("estado", "fecha_prestamo") 
    search_fields = ("socio__rut", "socio__user__username", "libro__titulo", 
"libro__isbn") 
    autocomplete_fields = ("socio", "libro") 