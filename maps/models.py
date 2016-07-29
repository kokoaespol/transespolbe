# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden, HttpResponse

#from django.core.mail import send_mail
# Create your models here.

class PosicionUsuario(models.Model):
  username = models.ForeignKey(User)
  latitud = models.FloatField()
  longitud = models.FloatField()

  def __unicode__(self):
    return unicode(self.username)

  class Meta:
    verbose_name = "Posicion Usuario"
    verbose_name_plural = "Posiciones Usuarios"

class Ruta(models.Model):
  nombre = models.CharField(max_length=100)
  entrada = models.BooleanField(default=False)
  salida = models.BooleanField(default=False)

  def __unicode__(self):
    return unicode(self.nombre)

  class Meta:
    verbose_name = "Ruta"
    verbose_name_plural= "Rutas"


class Conductor(models.Model):
  nombre = models.TextField(max_length=100)
  cedula = models.TextField(max_length=10)

  def __unicode__(self):
    return unicode(self.nombre)

  class Meta:
    verbose_name = "Conductor"
    verbose_name_plural = "Conductores"


class Bus(models.Model):
  nDisco = models.TextField(max_length=10)
  tipo = models.TextField(max_length=10,blank=True , null = True)
  marca = models.TextField(max_length=25,blank=True , null = True)
  placa = models.TextField(max_length = 15,blank=True , null = True)
  modelo = models.TextField(max_length = 30,blank=True , null = True)
  cSentados = models.IntegerField(max_length = 2,blank=True , null = True)
  cParados = models.IntegerField(max_length = 2,blank=True , null = True)

  def __unicode__(self):
    return unicode(self.nDisco)

  class Meta:
    verbose_name = "Bus"
    verbose_name_plural = "Buses"


class PosicionBus(models.Model):
  bus = models.ForeignKey(Bus, related_name = 'PosicionBus')
  fecha = models.DateTimeField()
  latitud = models.FloatField()
  longitud = models.FloatField()

  def __str__(self):
    return str(self.bus.nDisco)

  def __unicode__(self):
    return unicode(self.bus.nDisco)

  class Meta:
    verbose_name = "Posicion Bus"
    verbose_name_plural = "Posiciones Buses"

class Horario(models.Model):
  ruta = models.ForeignKey(Ruta, related_name = 'Horario')
  bus = models.ForeignKey(Bus, related_name = 'Horario')
  conductor = models.ForeignKey(Conductor, related_name = 'Horario')
  creador = models.ForeignKey(User, related_name = 'Horario')
  fecha = models.DateTimeField(auto_now = True)

  def __unicode__(self):
    return unicode(str(self.fecha) + ' --- ' + str(self.creador.username))

  class Meta:
    verbose_name = "Horario"
    verbose_name_plural= "Horarios"

class Publicacion(models.Model):
  username = models.ForeignKey(User, related_name='Publicacion')
  fecha = models.DateTimeField(auto_now_add=True)
  descripcion = models.CharField(max_length=250)
  foto = models.ImageField(upload_to='img_mensaje')

  def __unicode__(self):
    return unicode('user: ' + self.username + \
        'msg: ' + self.descripcion)

    class Meta:
      verbose_name = "Mensaje"
      verbose_name_plural= "Mensajes"
