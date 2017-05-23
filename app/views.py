from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.template import RequestContext
from django.template.loader import get_template
from app.models import aparcamiento, CSS, comentario, seleccionado
from app.xml_parse import getAparcamientos
from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags
from django.contrib.auth.hashers import make_password


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
    lista_5 = []
    aparcamientos_populares = aparcamiento.objects.annotate(quantity=Count('comentario')).order_by('-quantity')
    if aparcamientos_populares[0].quantity > 0:
        for contador in range(5):
            if aparcamientos_populares[contador].quantity > 0:
                print(aparcamientos_populares[contador])
                parking = aparcamiento.objects.get(nombre=aparcamientos_populares[contador])
                lista_5 += {parking}
    #CONSTRUYE LISTA DE URL's DE USERS
    user_list = []
    users = User.objects.all()
    for user in users:
        if str(user) != "superuser":
            config = CSS.objects.get(user=user)
            user_list += [(user, config.title)]
    #CONTRUYE EL HTML
    template = get_template('index.html')
    context = RequestContext(request, {'aparcamientos_populares' : lista_5, 'users' : user_list})

    return HttpResponse(template.render(context))

def aparcamientos_todos(request):
    parking_list = aparcamiento.objects.all()
    #CONTRUYE EL HTML
    template = get_template('aparcamientos.html')
    context = RequestContext(request, {'parking_list' : parking_list})
    return HttpResponse(template.render(context))

def aparcamiento_individual(request, id):
    parking = aparcamiento.objects.get(id=id)
    #CONTRUYE EL HTML
    template = get_template('aparcamiento.html')
    context = RequestContext(request, {'parking' : parking})
    return HttpResponse(template.render(context))

@csrf_exempt
def auth(request):
    if request.method == "POST":
        username = strip_tags(request.POST.get('username'))
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        return HttpResponseRedirect('/')
    else:
        template = get_template('index.html')
        return HttpResponseNotFound(template.render())

def register(request):
    if request.method == "GET":
        template = get_template('register.html')
        context = RequestContext(request, {})
        return HttpResponse(template.render(context))
    elif request.method == "POST":
        username = strip_tags(request.POST.get('username'))
        password = make_password(request.POST.get('password'))
        title = "Pagina de " + username
        user = User(username=username, password=password)
        user.save()
        user = User.objects.get(username=username)
        config = CSS(user=user, title=title, color='#808080', size=1)
        config.save()
        return HttpResponseRedirect("/")
    else:
        template = get_template('index.html')
        return HttpResponseNotFound(template.render())

def userpage(request, user):
    #CONSTRUYE LISTA DE URL's DE USERS
    user_list = []
    users = User.objects.all()
    for user in users:
        if str(user) != "superuser":
            config = CSS.objects.get(user=user)
            user_list += [(user, config.title)]
    #CONTRUYE EL HTML
    template = get_template('userPage.html')
    context = RequestContext(request, {'hotels' : 'PUTA','users' : user_list})
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
