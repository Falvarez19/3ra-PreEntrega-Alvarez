from django.db import models

# Create your models here.
from django.db import models

class Categoria(models.Model): #aca creamos la clase categoria dentro de model, esto representa las categorias de los productos
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Producto(models.Model): #aca tenemos la clase producto representa los productos a la venta
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Cliente(models.Model): #aca la clase cliente sostiene la info del cliente
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    direccion = models.TextField()

    def __str__(self):
        return self.nombre
