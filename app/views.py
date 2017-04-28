from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main(request):
    return HttpResponse("Hola")

def aparcamientos(request):
    return HttpResponse("aparcamientos")

def about(request):
    return HttpResponse("about")
