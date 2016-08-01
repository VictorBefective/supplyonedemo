"""supplyonedemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from users.views import (login_view, tablero, alta_proveedor,
	ver_proveedor, ordenes, proveedores, orden, logout_view)
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login_view),
    url(r'^logout/', logout_view),
    url(r'^proveedores/ver/(?P<id_proveedor>[0-9]+)/$', ver_proveedor),
    url(r'^orden/(?P<id_orden>[0-9]+)/$', orden),
    url(r'^proveedores/alta/', alta_proveedor),
    url(r'^proveedores/', proveedores),
    url(r'^solicitudes/', ordenes),
    url(r'^$',tablero),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
