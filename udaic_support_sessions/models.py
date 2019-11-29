from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.urls import reverse

__author__ = 'Fernando Andres Pretel'

# Create your models here.

#TODO: check for a better solution

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class SupportPerson(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user))
    name = models.CharField(null=True, max_length=200)
    last_name = models.CharField(null=True, max_length=200)

    class Meta:
        verbose_name = "Usuario UdAIC"
        verbose_name_plural = "Usuarios UdAIC"

    def __str__(self):
        texto = "Usuario UdAIC: %s" % self.name % self.last_name
        return texto


class BaseSupport(models.Model):
    id = models.AutoField(primary_key=True)
    client_user = models.ManyToManyField(SupportPerson, blank=True, null=True)
    support_user = models.ManyToManyField(SupportPerson, blank=True, null=True)
    title = models.CharField(null=True, max_length=200)
    creation_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=255)

    def get_absolute_url(self):
        return reverse('asesoramiento_detalle', (),
                {
                    'slug': self.slug,
                })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BaseSupport, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Asesoramiento Base"
        verbose_name_plural = "Asesoramientos Base"

    def __str__(self):
        texto = "Asesoramiento base: %s" % self.title
        return texto


class SupportSession(models.Model):
    base_support = models.ForeignKey(BaseSupport, on_delete=models.CASCADE)
