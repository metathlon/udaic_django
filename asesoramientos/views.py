from django.shortcuts import render
from django.http import HttpResponse
import rpy2

# Create your views here.

def home(request):
    return HttpResponse('<h1> ASESORAMIENTOS </h1>' + rpy2.__version__)