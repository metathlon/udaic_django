from django.urls import path

from . import views

app_name = 'asesoramientos'
urlpatterns = [
    path('', views.home, name='home'),
    ]