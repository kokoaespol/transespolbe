from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import generics


#class UsuarioViewSet(viewsets.ModelViewSet):
#    serializer_class = UsuarioSerializer
#    queryset = Usuario.objects.all()

class PosicionUsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = PosicionUsuarioSerializer
    queryset = PosicionUsuario.objects.all()

class PosicionBusViewSet(viewsets.ModelViewSet):
    serializer_class = PosicionBusSerializer
    queryset = PosicionBus.objects.all()

class PublicacionViewSet(viewsets.ModelViewSet):

    serializer_class = PublicacionSerializer
    queryset = Publicacion.objects.all()

class ConductorViewSet(viewsets.ModelViewSet):
    serializer_class = ConductorSerializer
    queryset = Conductor.objects.all()

class BusViewSet(viewsets.ModelViewSet):
    serializer_class = BusSerializer
    queryset = Bus.objects.all()

class HorarioViewSet(viewsets.ModelViewSet):
    serializer_class = HorarioSerializer
    queryset = Horario.objects.all()

    def get_queryset(self):
        import datetime
        horario = []
        date = datetime.date.today()
        start_week = date - datetime.timedelta(date.weekday())
        end_week = start_week + datetime.timedelta(7)
        rutas = Ruta.objects.all().order_by('nombre')
        horario = Horario.objects.filter(fecha__range=[start_week, end_week])
        return horario
