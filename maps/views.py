from django.shortcuts import render,render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from suds.xsd.doctor import ImportDoctor, Import
from suds.client import Client
from django.views.decorators.cache import never_cache
from django.core import serializers

from models import *
import json


# Create your views here.
@never_cache
def home(request):
    user = request.user
    if user.is_authenticated():
        return redirect('/maps/rutanorte1')
    else:
        return render(request,'login.html')

def login_web(request):
    if request.method == 'POST':
        try:
            user = request.POST['user']
            pwd = request.POST['pwd']
        except:
            return HttpResponseBadRequest('Error parametros')
        from django.contrib.auth import authenticate, login
        auth = authenticate(username = user , password = pwd)
        if auth is not None:
            login(request, auth)
        else:
            url = 'http://ws.espol.edu.ec/saac/wsandroid.asmx?WSDL'
            imp = Import('http://www.w3.org/2001/XMLSchema')
            imp.filter.add('http://tempuri.org/')
            doctor = ImportDoctor(imp)
            client = Client(url, doctor=doctor)
            auth = client.service.autenticacion(user,pwd)
            if auth == True:
                auth = User.objects.create_user(username=user, password=pwd)
                auth.save()
                auth = authenticate(username = user , password = pwd)
                #auth = User.objects.filter(username = user)
                login(request,auth)
            else:
                #self.username = None
                #self.password = None
                return HttpResponseForbidden('Autenticacion Fallida')
        return HttpResponse()

@never_cache
def login(request):

    status = 0
    auth_pk = 0

    try:
        user = request.GET['user'].strip()
        pwd = request.GET['pwd'].strip()
    except:
        return HttpResponseBadRequest('Error parametros')

    from django.contrib.auth import authenticate, login
    auth = authenticate(username = user , password = pwd)

    if auth is not None:
        login(request, auth)
        auth_pk = auth.pk
    else:
        url = 'http://ws.espol.edu.ec/saac/wsandroid.asmx?WSDL'
        imp = Import('http://www.w3.org/2001/XMLSchema')
        imp.filter.add('http://tempuri.org/')
        doctor = ImportDoctor(imp)
        client = Client(url, doctor=doctor)
        auth = client.service.autenticacion(user,pwd)
        if auth == True:
            auth = User.objects.create_user(username=user, password=pwd)
            auth.save()
            auth = authenticate(username = user , password = pwd)
            #auth = User.objects.filter(username = user)
            login(request,auth)
            auth_pk = auth.pk
            status = 202

            #return HttpResponse(auth.pk,status=202)
        else:
            #self.username = None
            #self.password = None
            return HttpResponseForbidden('Autenticacion Fallida')

    return HttpResponse(auth_pk,status=status)

@never_cache
def logout(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('/')

@never_cache
def index(request):

    busesdj = Bus.objects.all()
    posicionesdj = PosicionBus.objects.all()
    context = {
            'posicionesdj': posicionesdj,
            'busesdj': busesdj
            }
    return render(request, 'base.html', context)

#inspecciones = PosicionBus.objects.all()
    #buses = Bus.objects.all()
    #context = {'inspecciones': inspecciones,
    #           'buses': buses}
    #return render(request, 'base.html', context)

@never_cache
def map_web(request):

    rutas = Ruta.objects.all()
    bus = Bus.objects.all()
    #user = User.objects.get(pk=request.GET['us'])
    #inspecciones = PosicionUsuario.objects.filter(username=user)
    context = {'rutas': rutas,}

    return render(request, 'map_web.html', context)

@never_cache
def rutanorte1(request):

    #buses = PosicionBus.objects.raw('select * from ')
    return render(request, 'rutanorte1.html')

@never_cache
def map_mobil(request):

    ruta_map = request.GET['ruta'].strip()
    ruta_bus = ruta_map.split('-')[0]

    #import re
    #ruta_bus = str(re.split('(\d+)',ruta_bus)[0].lower())

    context = {'ruta_map':ruta_map,'ruta_bus':ruta_bus}
    return render(request, 'map_mobil.html',context)

@never_cache
def bus_position(request):

    pk_ruta = request.GET['ruta_bus'].strip()

    posicionbus_ruta = []
    buses = Bus.objects.filter(ruta=int(pk_ruta))

    try:
        #raw = 'select mp.* from maps_posicionbus mp, maps_bus mb where mp.bus_id=mb.id and mb.id=1 group by bus_id'
        raw = 'select * from maps_posicionbus group by bus_id'
        posicionbus = PosicionBus.objects.raw(raw)

        for b in list(buses):
            for bp in list(posicionbus):
                if bp.bus.id == b.id:
                    posicionbus_ruta.append(bp)
                    break


        #query = PosicionBus.objects.filter(bus_id=b.id).order_by('-bus_id')[:2]

    except:
        return HttpResponseBadRequest('BD conflictos, Notificar.')

    data = {'posicionbus_ruta': posicionbus_ruta}
    response = render_to_response(
            'json/positions.json',
            data,
            context_instance=RequestContext(request)
            )

    #from . import serializers
    #response = HttpResponse(json.dumps(serializers.posicionbus(buses_positions)))

    response['Content-Type'] = 'application/json; charset=utf-8'
    response['Cache-Control'] = 'no-cache'
    return response


"""
@never_cache
def logout(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('/')

"""
@never_cache
def ajax_route(request):
    route_type = str(request.GET['route'].strip())

    try:

        if route_type:
            if route_type == 'entrada':
                routes = Ruta.objects.filter(entrada=True)
            elif route_type == 'salida':
                routes = Ruta.objects.filter(salida=True)
    except:
        print( 'Error BD en Filter')

    data = {'routes': routes}
    response = render_to_response(
            'json/routes.json',
            data,
            context_instance=RequestContext(request)
            )

    response['Content-Type'] = 'application/json; charset=utf-8'
    response['Cache-Control'] = 'no-cache'
    return response

@never_cache
def administrator(request):
    bus = Bus.objects.all()
    return render(request,'administrator.html')

def tracking(request):
    route_type = request.GET['route'].strip()
    try:
        id_route = Ruta.objects.get(nombre = str(route_type.split('-')[0])).id
    except:
        return HttpResponseBadRequest()

    context = {'route_map':route_type,'id_route':id_route}
    return render(request,'tmp.html',context)

def horario(request):
    if request.method == 'GET':
        import datetime
        horario = []
        date = datetime.date.today()
        start_week = date - datetime.timedelta(date.weekday())
        end_week = start_week + datetime.timedelta(7)
        rutas = Ruta.objects.all().order_by('nombre')
        horario = Horario.objects.filter(fecha__range=[start_week, end_week])
        response = {'horario':horario,'inicio_semana':start_week,'final_semana':end_week,'rutas':rutas}
        return render(request,'horario.html',response)
    elif request.method == 'POST':
        ruta = request.POST.get('ruta',None)
        bus = request.POST.get('bus',None)
        conductor = request.POST.get('conductor',None)
        creador = request.user
        if ruta is None or bus is None or conductor is None or creador is None:
            return HttpResponseBadRequest()
        ruta = Ruta.objects.get(id = ruta)
        bus = Bus.objects.get(id = bus)
        conductor = Conductor.objects.get(id = conductor)
        horario = Horario(ruta= ruta, bus = bus, conductor = conductor, creador = creador)
        horario.save()
        return HttpResponse(status=200)

def planificador(request):
    buses = Bus.objects.all()
    conductores = Conductor.objects.all()
    rutas = Ruta.objects.all().order_by('nombre')
    return render(request, 'planificador.html',{'buses':buses,'conductores':conductores
        ,'rutas':rutas})

def manager(request):
    buses = Bus.objects.all()
    rutas = Ruta.objects.all()
    conductores = Conductor.objects.all()
    response = {
            'buses':buses,
            'rutas':rutas,
            'conductores':conductores
            }
    template = 'dashboard.html'
    return render(request,template, response)

def reporte(request):
    if request.method == 'GET':
        #Km/day
        buses = Bus.objects.all()
        result = []
        return render(request, 'reporte.html', {})


