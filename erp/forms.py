# -*- coding: utf-8 -*-
from django import forms
from crispy_forms.bootstrap import Field
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div

from .models import Cotizacion, Trabajo, Documentacion, Factura, OT


# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapModelForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
            self.fields[field_name].widget.attrs['required'] = 'required'

            if self.fields[field_name].widget.__class__.__name__ == forms.DateInput.__class__.__name__:
                self.fields[field_name].widget.attrs['id'] += 'datepicker'

# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

class FacturaModelForm(forms.ModelForm):
<<<<<<< HEAD
	class Meta:
		model = Factura
		fields = ('numero','fecha','observacion','cotizaciones')
		widgets = {'fecha': forms.DateInput(attrs={'id': 'datetimepicker12'})}
=======
    class Meta:
        model = Factura
        fields = ('numero','fecha','observacion','cotizaciones')
>>>>>>> 0e438ef8a1e3c01e66c3cac61a85f1d8072f67c4

# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

class OtForm(forms.ModelForm):
<<<<<<< HEAD
	class Meta:
		model = OT
		fields = ('numero','fecha','encargado', 'observacion')
		widgets = {'fecha': forms.DateInput(attrs={'id': 'datetimepicker12'})}
=======
    class Meta:
        model = OT
        fields = ('numero','fecha','encargado')
>>>>>>> 0e438ef8a1e3c01e66c3cac61a85f1d8072f67c4

# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\			

class DocumentacionForm(forms.ModelForm):
    class Meta:
        model = Documentacion
        fields = ('documento','fecha', 'numero')
        widgets = {'fecha': forms.DateInput(attrs={'id': 'datetimepicker12'})}

    def __init__(self, *args, **kwargs):
        super(DocumentacionForm, self).__init__(*args, **kwargs)
        if self.instance.id:
            self.fields['documento'].widget.attrs['readonly'] = True
        self.can_delete = False
        self.helper = FormHelper()
        # self.helper.form_tag = False
        self.helper.form_id = 'id-documentacion-form'
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.form_action = 'submit-uniform'

# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

class CotizacionForm(forms.ModelForm):
<<<<<<< HEAD
	class Meta:
		model = Cotizacion
		fields = ('fecha', 'local','detalle_monto', 'observacion',)
		widgets = {'fecha': forms.DateInput(attrs={'id': 'datetimepicker12'})}

	def __init__(self, *args, **kwargs):
		super(CotizacionForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False
		self.helper.form_read_only = True
		self.helper.form_id = 'id-cotizacion-form'
		self.helper.form_method = 'post'
		self.helper.form_action = 'submit-uniform'
		self.helper.layout = Layout(
					'fecha', 'local','detalle_monto',
					# Div(Field('estado_cotizacion', readonly=True, disabled=True), css_class="col-md-6"),
					Field('observacion',style="max-height: 100px;")
				)
					
=======
    class Meta:
        model = Cotizacion
        fields = ('fecha', 'local','estado_cotizacion','estado_trabajo','detalle_monto', 'observacion',)
        widgets = {'fecha': forms.DateInput(attrs={'id': 'datetimepicker12'})}

    def __init__(self, *args, **kwargs):
        super(CotizacionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_id = 'id-cotizacion-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit-uniform'
        self.helper.layout = Layout(
                    Div('fecha', 'local','detalle_monto', css_class="col-md-6"),
                    Div('estado_trabajo','estado_cotizacion', css_class="col-md-6"),
                    Field('observacion',style="max-height: 100px;")
                )

>>>>>>> 0e438ef8a1e3c01e66c3cac61a85f1d8072f67c4
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

class TrabajoForm(forms.ModelForm):
    class Meta:
        model = Trabajo
        fields = ('descripcion','unidad','valor','actividad','cuadrilla','cotizacion')

    def __init__(self, *args, **kwargs):
        super(TrabajoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_id = 'id-trabajo-form'
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'

# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

class TrabajoOTForm(forms.ModelForm):
<<<<<<< HEAD
	class Meta:
		model = Trabajo
		fields = ('ot', 'cotizacion', 'descripcion')

	def __init__(self, *args, **kwargs):
		super(TrabajoForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False
		self.helper.form_id = 'id-trabajo-form'
		self.helper.form_method = 'post'
		self.helper.form_class = 'form-inline'
		self.helper.field_template = 'bootstrap3/layout/inline_field.html'
=======
    class Meta:
        model = Trabajo
        fields = ('ot',)

    def __init__(self, *args, **kwargs):
        super(TrabajoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_id = 'id-trabajo-form'
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
>>>>>>> 0e438ef8a1e3c01e66c3cac61a85f1d8072f67c4
            
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

TrabajoFormSet = forms.inlineformset_factory(Cotizacion, Trabajo, form=TrabajoForm, extra=1)
TrabajoOTFormSet = forms.modelformset_factory(Trabajo, fields=['ot'], extra=0)				

DocumentacionFormset = forms.inlineformset_factory(Cotizacion, Documentacion, form=DocumentacionForm, extra=0)

# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

class CotizacionModelForm(forms.ModelForm):
<<<<<<< HEAD
	class Meta:
		model = Cotizacion
		fields = ('fecha', 'local','estado_cotizacion','detalle_monto', 'observacion',)
		widgets = {'fecha': forms.DateInput(attrs={'id': 'datetimepicker12'})}
=======
    class Meta:
        model = Cotizacion
        fields = ('fecha', 'local','estado_cotizacion','estado_trabajo','detalle_monto', 'observacion',)
        widgets = {'fecha': forms.DateInput(attrs={'id': 'datetimepicker12'})}
>>>>>>> 0e438ef8a1e3c01e66c3cac61a85f1d8072f67c4

# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

class TrabajoModelForm(forms.ModelForm):
    class Meta:
        model = Trabajo

        fields = ('unidad','valor','actividad','cuadrilla','cotizacion','descripcion')

# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\			
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\




















