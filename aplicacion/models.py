from django.db import models
from django.contrib.auth.models import User

    
class Adoptante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    historia = models.CharField(max_length=1000)
    perro = models.CharField(max_length=50)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Articulo(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    precio = models.IntegerField()

    class Meta:
        ordering = ['tipo']

    def __str__(self):
        return f"{self.nombre}"

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"
    
class Local(models.Model):
    direccion = models.CharField(max_length=50)
    horario_apertura = models.TimeField()
    horario_cierre = models.TimeField()
    partido = models.CharField(max_length=50)

    class Meta:
        ordering = ['partido']

    def __str__(self):
        return f"{self.direccion}"
    
class Perro(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField()
    tamanio = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    class Meta:
        ordering = ['tamanio']

    def __str__(self):
        return f"{self.nombre},{self.raza}"
