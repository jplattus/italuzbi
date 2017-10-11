from django.contrib import admin
import locale

# Register your models here.
from .models import Cliente, Factura, Pago, Local, Cotizacion, Encargado, OT, OC, Actividad, Cuadrilla, Estructura_costo, Cuenta_contable, Trabajo, Trabajador, Ejecuta, Proveedor, Material, Compra, Detalle_compra, Utilizado, Documento, Documentacion



class FacturaAdmin(admin.ModelAdmin):
	list_display = ('numero', str('fecha'), str('estado'), 'created_by',)
	ordering = ('fecha',)


class LocalAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'nombre_2', 'direccion', 'cliente')
	ordering = ('cliente',)

class CotizacionAdmin(admin.ModelAdmin):
	list_display = (
		'id',
		str('fecha'),
		'estado_cotizacion',
		'estado_trabajo',
		'local',
		'neto'
		)
	ordering = ('id',)

class DocumentoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'cliente')
	ordering = ('nombre',)

class DocumentacionAdmin(admin.ModelAdmin):
	list_display = ('cotizacion', 'documento', 'numero', 'fecha')
	ordering = ('cotizacion',)


admin.site.register(Documentacion, DocumentacionAdmin)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Cliente)
admin.site.register(Factura, FacturaAdmin)
admin.site.register(Pago)
admin.site.register(Local, LocalAdmin)
admin.site.register(Cotizacion, CotizacionAdmin)
admin.site.register(Encargado)
admin.site.register(OT)
admin.site.register(OC)
admin.site.register(Actividad)
admin.site.register(Cuadrilla)
admin.site.register(Estructura_costo)
admin.site.register(Cuenta_contable)
admin.site.register(Trabajo)
admin.site.register(Trabajador)
admin.site.register(Ejecuta)
admin.site.register(Proveedor)
admin.site.register(Material)
admin.site.register(Compra)
admin.site.register(Detalle_compra)
admin.site.register(Utilizado)
