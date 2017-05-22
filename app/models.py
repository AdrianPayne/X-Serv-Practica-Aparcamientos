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

class CSS(models.Model):
    usuario= models.ForeignKey(User)
    titulo= models.TextField(default="Pagina de usuario")
    color= models.CharField(default="#808080", max_length=32)
    tamaño= models.IntegerField(default=1)

class comentario(models.Model):
    comentario = models.TextField(default="")
    fecha = models.DateField(auto_now_add=True)
    aparcamiento = models.ForeignKey('aparcamiento')
    usuario = models.ForeignKey(User)


class seleccionado(models.Model):
    aparcamiento = models.ForeignKey('aparcamiento')
    usuario = models.ForeignKey(User)
    fecha = models.DateField(auto_now_add=True)
