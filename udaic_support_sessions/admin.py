from django.contrib import admin

from .models import SupportPerson, SupportSession, BaseSupport

# Register your models here.
admin.site.register(SupportPerson)
admin.site.register(SupportSession)
admin.site.register(BaseSupport)