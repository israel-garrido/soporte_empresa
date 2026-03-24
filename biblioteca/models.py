# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Socio(models.Model):
    # OneToOne
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="socio")
    rut = models.CharField(max_length=12, unique=True)
    # Este campo se agrega después como ejercicio de migración
    # telefono = models.CharField(max_length=20, blank=True, default="")
    telefono = models.CharField(max_length=20, blank=True, default="")
 
    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} ({self.rut})"

class Editorial(models.Model):
    # OneToMany (se materializa por ForeignKey en Libro)
    nombre = models.CharField(max_length=120, unique=True)
    
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=80, unique=True)
    
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=160)
    isbn = models.CharField(max_length=20, unique=True)
    anio_publicacion = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    
    # OneToMany
    editorial = models.ForeignKey(Editorial, on_delete=models.PROTECT,
    related_name="libros")
    # ManyToMany básico
    categorias = models.ManyToManyField(Categoria, blank=True, related_name="libros")
    # ManyToMany con tabla intermedia manual
    socios = models.ManyToManyField(Socio, through="Prestamo", related_name="libros_prestados")
 
    def __str__(self):
        return f"{self.titulo} ({self.isbn})"

class Prestamo(models.Model):
    # Tabla intermedia manual (through)
    ESTADOS = (
        ("PRESTADO", "Prestado"),
        ("DEVUELTO", "Devuelto"),
        ("ATRASADO", "Atrasado"),
    )
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, related_name="prestamos")
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name="prestamos")
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default="PRESTADO")
 
    class Meta:
        constraints = [
            models.UniqueConstraint(
            fields=["socio", "libro", "fecha_prestamo"],
            name="uq_prestamo_socio_libro_fecha",
        )
    ]
    
    def __str__(self):
        return f"{self.socio} -> {self.libro} ({self.estado})"