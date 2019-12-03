from django.urls import  path
from . import views

app_name = 'udaic_profile'
urlpatterns = [
    path('', views.register, name='user_register'),
    ]