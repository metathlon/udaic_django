from django.contrib import admin
from .models import UdaicUser, UdaicClient

# Register your models here.
admin.site.register(UdaicUser)
admin.site.register(UdaicClient)