from django.urls import  path
from . import views

app_name = 'udaic_blog'
urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    ]