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
        for place in aparcamientos_list:
            try:
                nuevo_aparcamiento = aparcamiento(nombre = place["NOMBRE"],
                descripcion = place["DESCRIPCION"], accesibilidad= place["ACCESIBILIDAD"],
                url = place["CONTENT-URL"], barrio = place["BARRIO"],
                distrito = place["DISTRITO"], latitud = place["LATITUD"],
                longitud = place["LONGITUD"],telefono = place["TELEFONO"], email = place["EMAIL"])
            except KeyError:
                try:
                    nuevo_aparcamiento = aparcamiento(nombre = place["NOMBRE"],
                    descripcion = place["DESCRIPCION"], accesibilidad= place["ACCESIBILIDAD"],
                    url = place["CONTENT-URL"], barrio = place["BARRIO"],
                    distrito = place["DISTRITO"], latitud = place["LATITUD"],
                    longitud = place["LONGITUD"])
                except KeyError:
                    try:
                        nuevo_aparcamiento = aparcamiento(nombre = place["NOMBRE"],
                        descripcion = place["DESCRIPCION"], accesibilidad= place["ACCESIBILIDAD"],
                        url = place["CONTENT-URL"], barrio = place["BARRIO"],
                        distrito = place["DISTRITO"])
                    except KeyError:
                        try:
                            nuevo_aparcamiento = aparcamiento(nombre = place["NOMBRE"],
                            descripcion = place["DESCRIPCION"], accesibilidad= place["ACCESIBILIDAD"],
                            url = place["CONTENT-URL"])
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

    if request.method == "POST":
        placeaccess = request.POST.get('district')
        if placeaccess != "None":
            parking_list = aparcamiento.objects.filter(distrito=placeaccess)
        else:
            parking_list = aparcamiento.objects.all()
    else:
        parking_list = aparcamiento.objects.all()

    #CONTRUYE EL HTML
    template = get_template('aparcamientos.html')
    context = RequestContext(request, {'parking_list' : parking_list})
    return HttpResponse(template.render(context))

def accessparking(request):
    if request.method == "GET":
        ParkingAccess = aparcamiento.objects.filter(accesibilidad = '1')
    template = get_template("aparcamientos.html")
    context = RequestContext(request, {"parking_list" : ParkingAccess})
    return HttpResponse(template.render(context))

def aparcamiento_individual(request, id):
    parking = aparcamiento.objects.get(id=id)
    comments = comentario.objects.filter(aparcamiento=parking)
    currentRate = parking.rate
    currentQuantity = parking.cantidad
    body = parking.descripcion
    if request.method == "POST":
        comment = request.POST.get("comentarios")
        chosen = request.POST.get("parking")
        liked = request.POST.get("liked")
        repeated = False
        if liked == str(1):
            newRate = currentRate + 1
            parking.rate = newRate
            parking.save()
        if comment != None:
            user = User.objects.get(username=request.user.username)
            commentUsers = comentario.objects.filter(aparcamiento=parking)
            newQuantity = currentQuantity + 1
            parking.quantity = newQuantity
            parking.save()
            newComment = comentario(comentario=comment, aparcamiento=parking, usuario=user)
            newComment.save()
        if chosen != None:
            userCh = User.objects.get(username=request.user.username)
            newSelection = seleccionado(aparcamiento=parking, usuario=userCh)
            newSelection.save()
    body = parking.descripcion
    currentRate = parking.rate
    template = get_template('aparcamiento.html')
    context = RequestContext(request, {"parking" : parking, "body" : body, "comments" : comments, "currentRate" : currentRate})
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

def css(request):
    color = "#808080"
    size = 120
    if request.user.is_authenticated():
        user = User.objects.get(username=request.user.username)
        userConfig = CSS.objects.get(user=user)
        color = CSS.color
        size = CSS.size
    template = get_template("css/style.css")
    print("hola")
    context = RequestContext(request, {"color": color, "size": size})
    return HttpResponse(template.render(context), content_type="text/css")

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

def userpage(request, username):
    #CONSTRUYE LISTA DE SELECCIONADOS POR EL USER
    userPage = User.objects.get(username=username)
    userConfig = CSS.objects.all()
    try:
        userConfig = CSS.objects.get(user=userPage)
        print("POR AQUI")
    except CSS.DoesNotExist:
        userConfig.user = userPage
        userConfig.update()
    try:
        ParkingFavs = seleccionado.objects.filter(usuario=userPage)
        ParkingList = []
        for fav in ParkingFavs:
            ParkingList += [fav.aparcamiento]
    except ParkingFavs.DoesNotExist:
        ParkingList = ""
    #CONTRUYE EL HTML
    template = get_template("userPage.html")
    context = RequestContext(request, {"ParkingList" : ParkingList, "userPage" : userPage, "userConfig" : userConfig})
    return HttpResponse(template.render(context))

def userXML(request, userXML):
    ParkingList = []
    user = User.objects.get(username = userXML)
    ParkingFavs = seleccionado.objects.filter(usuario=user)
    ParkingList = []
    for fav in ParkingFavs:
        ParkingList += [fav.aparcamiento]
    context = RequestContext(request, {"ParkingList" : ParkingList})
    template = get_template("userXML.xml")
    return HttpResponse(template.render(context), content_type = "text/xml")

def about(request):
    #CONTRUYE EL HTML
    template = get_template('about.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))
