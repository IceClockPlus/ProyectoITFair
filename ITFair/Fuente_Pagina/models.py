from django.db import models

# Create your models here.
class Leccion(models.Model):
    titulo = models.CharField(max_length=30)
    resumen = models.CharField(max_length=300)
    icono = models.ImageField(upload_to="iconos")
    video = models.CharField(max_length=100)

class ItemLeccion(models.Model):
    titulo = models.CharField(max_length=30)
    resumen = models.CharField(max_length=300)
    icono = models.ImageField(upload_to="iconos")
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE)