from django.conf.urls import patterns, url

# media files
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from maps import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #url(r'^login/$', views.login, name= 'login'),
    url(r'^web/', views.map_web, name='web'),
    url(r'^mobil', views.map_mobil, name='mobil'),
    url(r'^bus_position', views.bus_position, name='bus_position'),
    url(r'^manager/',views.manager, name='manager'),
)

#urlpatterns += staticfiles_urlpatterns()
