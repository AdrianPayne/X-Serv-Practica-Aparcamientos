from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main(request):
    loco = "hola"
    return render(request, 'app/base_index.html', {})

def aparcamientos(request):
    return HttpResponse("aparcamientos")

def about(request):
    return HttpResponse("about")
