# users/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UdaicUser


class UdaicUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = UdaicUser
        fields = ('username',)


class UdaicUserChangeForm(UserChangeForm):
    class Meta:
        model = UdaicUser
        fields = ('username',)