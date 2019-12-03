from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import UdaicUser, UdaicClient
from .forms import UdaicUserCreationForm, UdaicUserChangeForm


class UdaicUserAdmin(UserAdmin):
    add_form = UdaicUserCreationForm
    form = UdaicUserChangeForm
    model = UdaicUser
    list_display = ['username']


admin.site.register(UdaicUser, UdaicUserAdmin)
# admin.site.register(UdaicClient)
