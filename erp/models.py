from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.utils.encoding import python_2_unicode_compatible
import datetime

from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.	

class Factura(models.Model):
	
	EF = (
		(1,'Impaga'),
		(2,'Pagada'))

	numero = models.IntegerField()
	fecha = models.DateField()
	observacion = models.TextField(null=True)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True) 
	created_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	estado = models.IntegerField(choices=EF, default=1)
	cotizaciones = models.ManyToManyField('Cotizacion', null=True, blank=True)

	@property
	def neto(self):
		contador = 0
		for cotizacion in self.cotizaciones.all():
			contador += cotizacion.total
		return contador

	@property
	def iva(self):
		iva = self.neto * 0.19
		return iva

	@property
	def total(self):
		total = self.neto + self.iva
		return total

	def __str__(self):
		return str(self.numero)


class Cliente(models.Model):
	nombre = models.CharField(max_length=200)
	razon_social = models.CharField(max_length=200)
	giro = models.CharField(max_length=200)
	direccion_comercial = models.CharField(max_length=200)
	observacion = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)
	# created_by

	def __str__(self):
		return self.nombre

class Pago(models.Model):
	fecha = models.DateField()
	monto = models.IntegerField()
	facturas = models.ManyToManyField(Factura) 
	created_at = models.DateTimeField(auto_now_add=True, blank=True) 
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)
	# created_by

class Local(models.Model):
	nombre = models.CharField(max_length=200)
	nombre_2 = models.CharField(max_length=200, null=True)
	direccion = models.CharField(max_length=200)
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)
	# created_by
	def __str__(self):
		return self.nombre


class Cotizacion(models.Model):
	
	EC = (
		(1, 'En Espera'),
		(2,'Debe'),
		(3,'Por Facturar'),
		(4,'Facturada'))


	fecha = models.DateField()
	estado_cotizacion = models.IntegerField(choices=EC, default=1)
	local = models.ForeignKey(Local, on_delete=models.CASCADE)
	observacion = models.TextField(null=True)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)
	# created_by
	detalle_monto = models.BooleanField()	### <-- Para mostrar o no el detalle de monto por trabajo

	def __str__(self):
		return str(self.id)

	@property
	def neto(self):
		contador = 0
		for trabajo in Trabajo.objects.filter(cotizacion=self):
			contador += trabajo.total
		return contador

	@property
	def iva(self):
		iva = self.neto * 0.19
		return iva

	@property
	def total(self):
		total = self.neto + self.iva
		return total

	@property
	def debe(self):
		respuesta = True
		for doc in Documentacion.objects.filter(cotizacion=self):
			if doc.numero is None or doc.fecha is None:
				respuesta = False
				break
		return respuesta

	@property
	def trabajos_pendientes(self):
		respuesta = 0
		for trabajo in Trabajo.objects.filter(cotizacion=self):
			if trabajo.ot is None:
				respuesta += 1
		return respuesta

	@property
	def tiene_documento(self):
		respuesta = False
		for doc in Documentacion.objects.filter(cotizacion=self):
			if doc.documento:
				respuesta = True
				break
		return respuesta



	def get_absolute_url(self):
		return reverse('erp:cotizacion_edit', kwargs={'cotizacion_id': self.id})



class Encargado(models.Model):
	nombre = models.CharField(max_length=200)
	apellido = models.CharField(max_length=200)
	telefono = models.CharField(max_length=200)
	correo = models.CharField(max_length=200)
	rut = models.CharField(max_length=200)
	cargo = models.CharField(max_length=200)
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)
	# created_by

	def __str__(self):
		return self.nombre + " " + self.apellido + " - " + self.cargo + " en " + self.cliente.nombre

class OT(models.Model):
	numero = models.IntegerField()
	fecha = models.DateField()
	encargado = models.ForeignKey(Encargado, on_delete=models.CASCADE)
	observacion = models.TextField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)
	# created_by

	def __str__(self):
		return str(self.numero) 

class OC(models.Model):  # NO SE OCUPA
	numero = models.IntegerField()
	fecha_emision = models.DateField()
	documento_externo = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)
	# created_by
	cotizaciones = models.ManyToManyField(Cotizacion)

class Actividad(models.Model):
	nombre = models.CharField(max_length=50)
	observacion = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)
	# created_by

	def __str__(self):
		return self.nombre

class Cuadrilla(models.Model):
	nombre = models.CharField(max_length=50)
	observacion = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)
	# created_by
	def __str__(self):
		return self.nombre


class Estructura_costo(models.Model):
	nombre = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)
	# created_by
	def __str__(self):
		return self.nombre


class Cuenta_contable(models.Model):
	nombre = models.CharField(max_length=200)
	estructura_costo = models.ForeignKey(Estructura_costo, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)
	# created_by
	def __str__(self):
		return self.nombre





class Trabajo(models.Model):
	descripcion = models.CharField(max_length=200)
	unidad = models.IntegerField()
	valor = models.IntegerField()
	actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
	cuadrilla = models.ForeignKey(Cuadrilla, on_delete=models.CASCADE)
	cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
	ot = models.ForeignKey(OT, null=True, on_delete=models.CASCADE)
	observacion = models.TextField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)
	# created_by
	@property
	def total(self):
		return self.valor * self.unidad
	#valor_hora	### <- Para que era?
	def __str__(self):
		return self.descripcion



class Trabajador(models.Model):
	nombre = models.CharField(max_length=200)
	apellido = models.CharField(max_length=200)
	rut = models.CharField(max_length=200)
	telefono = models.CharField(max_length=200)
	correo = models.CharField(max_length=200)
	sueldo_base = models.FloatField()
	cuenta_contable = models.ForeignKey(Cuenta_contable, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)
	# created_by
	fecha_inicio_contrato = models.DateField()
	fecha_termino_contrato = models.DateField()
	horas_semanales = models.IntegerField()

	def __str__(self):
		return self.nombre + " " + self.apellido

class Ejecuta(models.Model):	### <-- Relacion Trabajador EJECUTA Trabajo
	
	puntaje=(
		(5,'Muy Bien'),
		(4,'Bien'),
		(3,'Suficiente'),
		(2,'Mal'),
		(1,'Muy Mal'))

	trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE)
	trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
	horas_trabajadas = models.IntegerField()
	observacion = models.TextField(null=True, blank=True)
	nota = models.IntegerField(choices=puntaje, default=3)

	def __str__(self):
		return self.trabajo.descripcion + " - " + self.trabajador.nombre + " " + self.trabajador.apellido


class Proveedor(models.Model):
	nombre = models.CharField(max_length=200)
	razon_social = models.CharField(max_length=200)
	giro = models.CharField(max_length=200)
	direccion_comercial = models.CharField(max_length=200)
	observacion = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)
	# created_by


class Material(models.Model):
	nombre = models.CharField(max_length=200)
	unidad = models.CharField(max_length=200)
	sku = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)
	# created_by

class Compra(models.Model):
	numero = models.IntegerField()
	fecha = models.DateField()
	neto = models.IntegerField()
	iva = models.IntegerField()
	proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)
	# created_by
	trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
	# documento  <- Para que era?????

### <-- Relacion DETALLE de la compra --> ###
class Detalle_compra(models.Model):		
	material = models.ForeignKey(Material, on_delete=models.CASCADE)
	compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
	cantidad = models.IntegerField()



class Utilizado(models.Model):	### <-- Relacion Material UTILIZADO en Trabajo
	material = models.ForeignKey(Material, on_delete=models.CASCADE)
	trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE)
	cantidad = models.IntegerField()

class Documento(models.Model):	
	nombre = models.CharField(max_length=200)
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre

class Documentacion(models.Model):	### <-- Documentacion necesaria para facturar la cotizacion
	cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
	documento = models.ForeignKey(Documento, on_delete=models.CASCADE, null=True, blank=True)
	numero = models.IntegerField(null=True, blank=True)
	fecha = models.DateField(null=True, blank=True)

	# def __str__(self):
	# 	return self.documento

















