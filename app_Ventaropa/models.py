from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    talla = models.CharField(max_length=10)
    color = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre} ({self.talla}, {self.color})"