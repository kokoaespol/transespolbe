from django.contrib import admin
from maps.models import *
#from apprest.models import *


# Register your models here.

#class InspeccionImagenInline(admin.TabularInline):
    #model = QuejaImagen
    #extra = 1

#class UsuarioSolicitudInline(admin.TabularInline):
#    model = UsuarioSolicitud
#    extra = 1
#
#class InspeccionAdmin(admin.ModelAdmin):
    #inlines = [ InspeccionImagenInline, ]

#class UsuarioAdmin(admin.ModelAdmin):
#    list_display = ['username']
    #search_fields = ['nombre', 'apellido', 'cedula', 'correo']
    #inlines = [ UsuarioSolicitudInline, ]

class PosicionUsuarioAdmin(admin.ModelAdmin):
    list_display = ['latitud','longitud']
    #list_filter = ['usuario']
    #search_fields = ['estado']

class PosicionBusAdmin(admin.ModelAdmin):
    list_display = ['latitud','longitud']
 
class ObjetoPerdidoAdmin(admin.ModelAdmin):
    list_display = ['username','fecha','descripcion']
 
class ConductorAdmin(admin.ModelAdmin):
    list_display = ['nombre','cedula']

class BusAdmin(admin.ModelAdmin):
    list_display = ['nDisco','tipo','placa']



#admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(PosicionUsuario, PosicionUsuarioAdmin)
admin.site.register(PosicionBus, PosicionBusAdmin)
admin.site.register(Conductor, ConductorAdmin)
admin.site.register(Bus, BusAdmin)
admin.site.register(Ruta)
admin.site.register(Horario)
admin.site.register(Publicacion)

#admin.site.register(Queja, InspeccionAdmin)
