from django.shortcuts import render
from .models import Libro

def lista_libros(request):
    libros = (
        Libro.objects
        .select_related("editorial")
        .prefetch_related("categorias")
        .order_by("titulo")
    )
    return render(request, "lista_libros.html", {"libros": libros})

def detalle_libro(request, libro_id):
    libro = (
        Libro.objects
        .select_related("editorial")
        .prefetch_related("categorias", "prestamos__socio__user")
        .get(id=libro_id)
    )
    
    prestamos = libro.prestamos.all().order_by("-fecha_prestamo")
    return render(request, "detalle_libro.html", {"libro": libro, "prestamos":prestamos})

#def index(request):
#    context = {}
#    return render(request, 'index.html', context)