# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.views import generic

from .forms import CotizacionForm, TrabajoFormSet, DocumentacionFormset, FacturaModelForm, OtForm, TrabajoOTFormSet
from .models import Cliente, Factura, Trabajo, Cotizacion, Documentacion, Documento, OT


@login_required
def index(request):
    template = loader.get_template('erp/index.html')
    return HttpResponse(template.render(request))


# ********************************************************************************************************************************************

class FacturasByUserListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user. 
    """
    model = Factura
    template_name ='erp/facturas_por_usuario.html'
    paginate_by = 30
    
    def get_queryset(self):
        return Factura.objects.filter(created_by=self.request.user).filter(estado__exact='1').order_by('fecha')

# ********************************************************************************************************************************************

class ListarTrabajosView(LoginRequiredMixin,generic.ListView):
    model = Trabajo
    template_name = 'erp/trabajos.html'
    paginate_by = 30

# ********************************************************************************************************************************************

class ListarCotizacionesFacturaView(LoginRequiredMixin,generic.ListView):
    template_name = 'erp/cotizaciones.html'
    paginate_by = 30
    def get_queryset(self):
        self.factura = get_object_or_404(Factura, id=self.args[0]) # Es para darle el argumento de la factura.
        return self.factura.cotizaciones.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListarCotizacionesFacturaView, self).get_context_data(**kwargs)
        # Add in the factura
        context['factura'] = self.factura
        return context
 
# ********************************************************************************************************************************************       

class ListarTrabajoCotizacionView(LoginRequiredMixin,generic.ListView):

    template_name = 'erp/trabajos.html'
    paginate_by = 30
    
    def get_queryset(self):
        self.cotizacion = get_object_or_404(Cotizacion, id=self.args[0]) # Es para darle el argumento de la cotizacion.
        return Trabajo.objects.filter(cotizacion=self.cotizacion)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListarTrabajoCotizacionView, self).get_context_data(**kwargs)
        # Add in the factura
        context['cotizacion'] = self.cotizacion
        return context
 
# ******************************************************************************************************************************************** 

class ListarCotizacionView(LoginRequiredMixin,generic.ListView):
    model = Cotizacion
    template_name = 'erp/cotizaciones.html'
    paginate_by = 30

# ********************************************************************************************************************************************

class ListarFacturaView(LoginRequiredMixin,generic.ListView):
    model = Factura
    template_name = 'erp/facturas.html'
    paginate_by = 30


# ********************************************************************************************************************************************
# CREAR FACTURA
# ********************************************************************************************************************************************

def factura_new(request, factura_id=None, *args, **kwargs):
    if factura_id:
        instancia = Factura.objects.get(pk=factura_id)
    else:
        instancia = Factura()
    form = FacturaModelForm(request.POST or None, prefix='factura',instance=instancia)
    if form.is_valid():
        form.save()
        for cotizacion in instancia.cotizaciones.all():
            cotizacion.estado_cotizacion = 4
            cotizacion.save()
        return redirect('erp:facturas')
    return render(request, 'erp/factura_form.html', {'form': form})

# ********************************************************************************************************************************************
# CREAR ORDEN DE TRABAJO
# ********************************************************************************************************************************************

def ot_new(request, ot_id=None, *args, **kwargs):

    if ot_id:
        instancia = OT.objects.get(pk=ot_id)
        trabajo_list = Trabajo.objects.filter(ot=ot_id)
    else:
        instancia = OT()
        trabajo_list = Trabajo.objects.exclude(ot__isnull=False)
    form = OtForm(request.POST or None, prefix='ot',instance=instancia)
    formset = TrabajoOTFormSet(request.POST, request.FILES, prefix='ot', instance=instancia)
    if form.is_valid():
        form.save()
        return redirect('erp:trabajos')
    return render(request, 'erp/ot_form.html', {'form': form , 'formset': formset , 'trabajo_list': trabajo_list})

    

# ********************************************************************************************************************************************

def documentacion_new(request, cotizacion_id=None, *args, **kwargs):
    if cotizacion_id:
        docus = Cotizacion.objects.get(pk=cotizacion_id)
        formset = DocumentacionFormset(prefix='documentacion',instance=docus)
        if request.method == 'POST':
            formset = DocumentacionFormset(request.POST, request.FILES, prefix='documentacion', instance=docus)
            documentacion_valid = formset.is_valid()
            if documentacion_valid:
                formset.save()
                if docus.debe:
                        docus.estado_cotizacion = 3
                        docus.save()                
                return redirect('erp:cotizacion_detail', pk=cotizacion_id)
    return render(request, 'erp/documentacion_form.html', {'formset': formset, 'cotizacion': docus})

# ********************************************************************************************************************************************

def cotizacion_new(request, cotizacion_id=None, *args, **kwargs):
    if cotizacion_id:
        editar = Cotizacion.objects.get(pk=cotizacion_id)
    else:
        editar = Cotizacion()
    if request.method == 'POST':
        cotizacion_form = CotizacionForm(request.POST, request.FILES, prefix='cotizacion', instance=editar)
        trabajo_forms = TrabajoFormSet(request.POST, request.FILES, prefix='trabajo', instance=editar)
        cotizacion_valid = cotizacion_form.is_valid()
        trabajo_valid = trabajo_forms.is_valid()
        if cotizacion_valid and trabajo_valid:
            cotizacion = cotizacion_form.save()
            trabajo_forms.instance = cotizacion
            trabajo_forms.save()
            if not editar.tiene_documento:
                for doc in Documento.objects.filter(cliente=cotizacion.local.cliente):
                    Documentacion.objects.create(cotizacion_id=cotizacion.pk, documento_id=doc.pk)    
            return redirect('erp:cotizacion_detail', pk=cotizacion.pk)
    else:
        cotizacion_form = CotizacionForm(prefix='cotizacion', instance=editar)
        trabajo_forms = TrabajoFormSet(prefix='trabajo', instance=editar)
    return render(request, 'erp/cotizacion_edit.html', {'cotizacion_form': cotizacion_form, 'trabajo_forms': trabajo_forms})

# ********************************************************************************************************************************************

class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Cotizacion
    template_name = 'erp/detail.html'


class ResultsView(generic.DetailView):
    model = Cliente
    template_name = 'erp/results.html'


def vote(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    try:
        selected_factura = cliente.factura_set.get(pk=request.POST['factura'])
    except (KeyError, Factura.DoesNotExist):
        # Redisplay the cliente voting form.
        return render(request, 'erp/detail.html', {
            'cliente': cliente,
            'error_message': "You didn't select a factura.",
        })
    else:
        selected_factura.estado = 'pagada'
        selected_factura.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('erp:results', args=(cliente.id,)))
