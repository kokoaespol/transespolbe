from rest_framework import serializers
from .models import *

#class UsuarioSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Usuario
#        fields = ('id','username', 'password',)

class PosicionUsuarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = PosicionUsuario
    fields = ('id', 'username', 'latitud', 'longitud',)

class PosicionBusSerializer(serializers.ModelSerializer):
  class Meta:
    model = PosicionBus
    field = ('','fecha','hora','latitud','longitud',)

class PublicacionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Publicacion
    field = ('id','username','fecha','descripcion',)

class ConductorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Conductor
    field = ('id','nombre','cedula',)

class BusSerializer(serializers.ModelSerializer):
  class Meta:
    model = Bus
    field = ('nDisco','conductor','tipo','marca','placa','modelo','cSentados','cParados',)

class HorarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Horario
    depth = 1
    field = ('bus','conductor','creador','fecha',)

def posicionbus(queryset):

  if not queryset:
    return []

  return [{
    'position_first': {
      'disco': pb[0].bus_id,
      'fecha': str(pb[0].fecha),
      'lat': pb[0].latitud,
      'lon': pb[0].longitud,
      },

    'position_second': {
      'disco': pb[1].bus_id,
      'fecha': str(pb[1].fecha),
      'lat': pb[1].latitud,
      'lon': pb[1].longitud,
      }

    } for pb in queryset ]

