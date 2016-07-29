from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from maps.viewsets import *
from rest_framework.routers import DefaultRouter
import maps

admin.autodiscover()
router = DefaultRouter()

#router.register(r'usuarios',UsuarioViewSet)
router.register(r'posicionesUsuarios',PosicionUsuarioViewSet)
router.register(r'conductor',ConductorViewSet)
router.register(r'bus',BusViewSet)
router.register(r'posicionBus', PosicionBusViewSet)
router.register(r'publicacion', PublicacionViewSet)
router.register(r'horario', HorarioViewSet)
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'maps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^maps/', include('maps.urls')),
    url(r'^login/','maps.views.login', name='login'),
    url(r'^login_web/','maps.views.login_web', name='login_web'),
    url(r'^logout/','maps.views.logout', name='logout'),
    url(r'^administrator/','maps.views.administrator',name='administrator'),
    url(r'^tracking/','maps.views.tracking',name='tracking'),
    url(r'^horario/','maps.views.horario',name='horario'),
    url(r'^ajax_route/',maps.views.ajax_route,name='ajax_route'),
 #   url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^planificador/','maps.views.planificador', name='planificador'),
    url(r'^reporte/','maps.views.reporte'),
) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
