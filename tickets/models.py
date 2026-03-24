# tickets/models.py 
from django.db import models 
 
class Ticket(models.Model): 
    PRIORIDAD_CHOICES = [ 
        ("BAJA", "Baja"), 
        ("MEDIA", "Media"), 
        ("ALTA", "Alta"), 
    ] 
 
    ESTADO_CHOICES = [ 
        ("ABIERTO", "Abierto"), 
        ("EN_PROCESO", "En proceso"), 
        ("CERRADO", "Cerrado"), 
    ] 
 
    titulo = models.CharField(max_length=120) 
    email_contacto = models.EmailField() 
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES, 
default="MEDIA") 
    estado = models.CharField(max_length=12, choices=ESTADO_CHOICES, 
default="ABIERTO") 
    descripcion = models.TextField(blank=True) 
    fecha_creacion = models.DateTimeField(auto_now_add=True) 
 
    def __str__(self): 
        return f"[{self.estado}] {self.titulo}" 