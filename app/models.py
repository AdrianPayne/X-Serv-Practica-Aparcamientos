from django.db import models
from django.contrib.auth.models import User

class aparcamiento(models.Model):
    nombre= models.TextField(default="")
    url= models.TextField(default="")
    descripcion= models.TextField(default="")
    barrio= models.TextField(default="")
    distrito= models.TextField(default="")
    accesibilidad= models.TextField(default="")
    latitud= models.FloatField(default=0)
    longitud= models.FloatField(default=0)
    telefono= models.TextField(default="")
    email= models.TextField(default="")
    cantidad = models.IntegerField(default = 0)
    rate = models.IntegerField(default = 0)
    def __str__(self):
        return self.nombre


class CSS(models.Model):
    user = models.ForeignKey(User, default="")
    title = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return str(self.user)

class comentario(models.Model):
    comentario = models.TextField(default="")
    fecha = models.DateField(auto_now_add=True)
    aparcamiento = models.ForeignKey('aparcamiento')
    usuario = models.ForeignKey(User)
    def __str__(self):
        return str(self.aparcamiento)


class seleccionado(models.Model):
    aparcamiento = models.ForeignKey('aparcamiento')
    usuario = models.ForeignKey(User)
    fecha = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.aparcamiento)
