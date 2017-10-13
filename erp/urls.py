# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

app_name = 'erp'
urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^misfacturas/$', views.FacturasByUserListView.as_view(), name='mis-facturas'),
    url(r'^trabajos/$', views.ListarTrabajosView.as_view(), name='trabajos'),
    url(r'^trabajos/ot/new/$', views.ot_new, name='ot_new'),
    url(r'^cotizaciones/$', views.ListarCotizacionView.as_view(), name='cotizaciones'),
    url(r'^cotizacion/new/$', views.cotizacion_new, name='cotizacion_new'),
    url(r'^cotizacion/new/documents/(?P<cotizacion_id>[0-9]+)/$', views.documentacion_new, name='cotizacion_new_documents'),
    url(r'^cotizacion/edit/(?P<cotizacion_id>[0-9]+)/$', views.cotizacion_new, name='cotizacion_edit'),
    url(r'^cotizacion/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='cotizacion_detail'),
    url(r'^cotizacion/trabajos/([\w-]+)/$', views.ListarTrabajoCotizacionView.as_view(), name='cotizacion_trabajos'),
    url(r'^factura/new/$', views.factura_new, name='factura_new'),
    url(r'^factura/edit/(?P<factura_id>[0-9]+)/$', views.factura_new, name='factura_new'),
    url(r'^factura/cotizaciones/([\w-]+)/$', views.ListarCotizacionesFacturaView.as_view(), name='cotizaciones_factura'),
    url(r'^facturas/$', views.ListarFacturaView.as_view(), name='facturas'),

    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<cliente_id>[0-9]+)/vote/$', views.vote, name='vote'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)