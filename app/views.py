from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main(request):
    loco = "hola"
    return render(request, 'base_index.html', {})

def aparcamientos(request):
    return HttpResponse("aparcamientos")


def aparcamiento(request, id):  #INDIVIDUAL
    return HttpResponse("APARCAMIENTO")

def usuario(request):
    return HttpResponse("USUARIO")

def usuarioXML(request):
    return HttpResponse("USUARIOXML")

def about(request):
    return HttpResponse("about")
