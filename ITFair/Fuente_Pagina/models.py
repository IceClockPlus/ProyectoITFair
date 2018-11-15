from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Leccion(models.Model):
    titulo = models.CharField(max_length=30,unique=True)
    resumen = models.CharField(max_length=300)
    icono = models.ImageField(upload_to="iconos")
    video = models.CharField(max_length=100)
    url = models.SlugField(max_length=100)

    def save(self, *args, **kwargs):
        self.url = slugify(self.titulo)
        super(Leccion, self).save(*args, **kwargs)

class ItemLeccion(models.Model):
    titulo = models.CharField(max_length=30)
    resumen = models.CharField(max_length=300)
    icono = models.ImageField(upload_to="iconos")
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE)