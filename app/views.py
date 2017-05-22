from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.template import RequestContext
from django.template.loader import get_template
from app.models import aparcamiento, CSS, comentario, seleccionado
from app.xml_parse import getAparcamientos


def main(request):

    aparcamientos_list = aparcamiento.objects.all()
    #COMPRUEBA SI SE HA PARSEADO EL XML => LO PARSEA
    if not aparcamientos_list:
        aparcamientos_list = getAparcamientos()
        for plaza in aparcamientos_list:
            try:
                nuevo_aparcamiento = aparcamiento(nombre = plaza["NOMBRE"],url = plaza["CONTENT-URL"],descripcion = plaza["DESCRIPCION"],
                barrio = plaza["BARRIO"],distrito = plaza["DISTRITO"],accesibilidad= plaza["ACCESIBILIDAD"],latitud = plaza["LATITUD"],
                longitud = plaza["LONGITUD"])
            except KeyError:
                continue
            nuevo_aparcamiento.save()
        
    #ORDENA POR COMENTARIOS

    #CONTRUYE EL HTML
    template = get_template('index.html')
    context = RequestContext(request, {'hotels' : 'PUTA'})

    return HttpResponse(template.render(context))

def aparcamientos_todos(request):
    #CONTRUYE EL HTML
    template = get_template('index.html')
    context = RequestContext(request, {'hotels' : 'PUTA'})
    return HttpResponse(template.render(context))

def aparcamiento_individual(request, id):
    #CONTRUYE EL HTML
    template = get_template('index.html')
    context = RequestContext(request, {'hotels' : 'PUTA'})
    return HttpResponse(template.render(context))

def usuario(request):
    #CONTRUYE EL HTML
    template = get_template('index.html')
    context = RequestContext(request, {'hotels' : 'PUTA'})
    return HttpResponse(template.render(context))

def usuarioXML(request):
    #CONTRUYE EL HTML
    template = get_template('index.html')
    context = RequestContext(request, {'hotels' : 'PUTA'})
    return HttpResponse(template.render(context))

def about(request):
    #CONTRUYE EL HTML
    template = get_template('index.html')
    context = RequestContext(request, {'hotels' : 'PUTA'})
    return HttpResponse(template.render(context))
