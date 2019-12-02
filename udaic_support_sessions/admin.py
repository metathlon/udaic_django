from django.contrib import admin

from .models import SupportSession, BaseSupport

# Register your models here.

admin.site.register(SupportSession)
admin.site.register(BaseSupport)