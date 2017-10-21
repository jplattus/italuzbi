from .models import Cotizacion, Trabajo

def add_variable_to_context(request):
    contador_cotizaciones = Cotizacion.objects.filter(estado_cotizacion = 4).count()
    contador_trabajos_sin_ot = Trabajo.objects.filter(ot = None).count()

    return {
        'contador_cotizaciones': contador_cotizaciones, 'contador_trabajos_sin_ot': contador_trabajos_sin_ot
    }