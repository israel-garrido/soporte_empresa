from django.urls import path
from . import views

urlpatterns = [
 path("libros/", views.lista_libros, name="lista_libros"),
 path("libros/<int:libro_id>/", views.detalle_libro, name="detalle_libro"),
]