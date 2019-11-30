from django.db import models
from udaic_profile.models import UdaicUser

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(null=True, max_length=200)
    text = models.TextField(null=True)
    author = models.ForeignKey(UdaicUser, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Articulo Blog"
        verbose_name_plural = "Artículos Blog"
