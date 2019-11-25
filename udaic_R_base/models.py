from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

__author__ = 'Fernando Andres Pretel'

# Create your models here.


class PersonaAsesoramiento(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, default=1)
    nombre = models.CharField(null=True, max_length=200)
    apellidos = models.CharField(null=True, max_length=200)

    class Meta:
        verbose_name = "usario UdAIC"
        verbose_name_plural = "usuarios UdAIC"

    def __str__(self):
        texto = "Usuario UdAIC: %s" % self.nombre % self.apellidos
        return texto


class Asesoramiento(models.Model):
    usuario_asesorado = models.ForeignKey(PersonaAsesoramiento.id, blank=True, null=True)
    usuario_asesor = models.ForeignKey(PersonaAsesoramiento.id, blank=True, null=True, on_delete=models.CASCADE)
    asunto = models.CharField(null=True, max_length=200)
    creation_date = models.DateField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = "asesoramiento base"
        verbose_name_plural = "asesoramientos base"

    def __str__(self):
        texto = "Asesoramiento base: %s" % self.asunto
        return texto

