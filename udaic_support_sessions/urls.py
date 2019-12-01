from django.urls import path

from . import views

app_name = 'udaic_support_sessions'
urlpatterns = [
    path('', views.asesoramientos_home, name='asesoramientos_home'),
    ]