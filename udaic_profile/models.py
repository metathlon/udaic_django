from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UdaicUser(AbstractUser):
    name = models.CharField(null=True, max_length=200)
    last_name = models.CharField(null=True, max_length=200)
    email = models.EmailField(null=True)

    is_member = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Usuario Genérico UdAIC"
        verbose_name_plural = "Usuarios Genéricos UdAIC"

    def __str__(self):
        texto = "Usuario UdAIC: %s %s" % (self.name, self.last_name)
        return texto


class UdaicClient(models.Model):
    user = models.OneToOneField(UdaicUser, on_delete=models.CASCADE, primary_key=True)
    servicio = models.CharField(null=True, max_length=200)

    class Meta:
        verbose_name = "Asesorado de UdAIC"
        verbose_name_plural = "Asesorados de UdAIC"

    def __str__(self):
        texto = "Asesorado UdAIC: %s %s" % (self.user.name, self.user.last_name)
        return texto

