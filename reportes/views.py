from django.shortcuts import render
from django.db.models import Q
from polizas.models import Poliza
from core.models import Detalleagas, Detalleastp
from django.contrib.auth.decorators import login_required

@login_required
def menu(request):
    return render(request, "reportes/menu.html")

@login_required
def reporte_polizas(request):
    query = request.GET.get('q')
    polizas = Poliza.objects.select_related(
        'clienteid', 'agenteid', 'aseguradoraid', 'tipopolizaid', 'formapagoid', 'metodopagoid'
    )

    if query:
        terms = query.split()  # Ejemplo: "Juan Pérez" → ["Juan", "Pérez"]
        q_objects = Q()

        for term in terms:
            q_objects |= Q(id__icontains=term)
            q_objects |= Q(clienteid__nombre__icontains=term)
            q_objects |= Q(clienteid__appaterno__icontains=term)
            q_objects |= Q(clienteid__apmaterno__icontains=term)
            q_objects |= Q(agenteid__nombre__icontains=term)
            q_objects |= Q(agenteid__apellidopaterno__icontains=term)
            q_objects |= Q(agenteid__apellidomaterno__icontains=term)
            q_objects |= Q(aseguradoraid__nombre__icontains=term)
            q_objects |= Q(tipopolizaid__nombre__icontains=term)
            q_objects |= Q(formapagoid__forma__icontains=term)
            q_objects |= Q(metodopagoid__metodo__icontains=term)

        polizas = polizas.filter(q_objects).order_by('fechafin')
    else:
        polizas = polizas.order_by('fechafin')

    return render(request, "reportes/polizas.html", {'polizas': polizas})

@login_required
def reporte_AgAs(request):
    query = request.GET.get('q')
    detalles = Detalleagas.objects.select_related(
        'agenteid', 'aseguradoraid'
    )

    if query:
        terms = query.split()  # Ejemplo: "Juan Pérez" → ["Juan", "Pérez"]
        q_objects = Q()

        for term in terms:
            # 🔸 Búsqueda por datos del agente
            q_objects |= Q(agenteid__id__icontains=term)
            q_objects |= Q(agenteid__nombre__icontains=term)
            q_objects |= Q(agenteid__apellidopaterno__icontains=term)
            q_objects |= Q(agenteid__apellidomaterno__icontains=term)

            # 🔸 Búsqueda por datos de la aseguradora
            q_objects |= Q(aseguradoraid__id__icontains=term)
            q_objects |= Q(aseguradoraid__nombre__icontains=term)

        detalles = detalles.filter(q_objects).order_by(
            'agenteid__nombre',
            'agenteid__apellidopaterno',
            'agenteid__apellidomaterno'
        )
    else:
        detalles = detalles.order_by(
            'agenteid__nombre',
            'agenteid__apellidopaterno',
            'agenteid__apellidomaterno'
        )

    return render(request, "reportes/AgAs.html", {'detalles': detalles})

@login_required
def reporte_AsTP(request):
    query = request.GET.get('q')
    detalles = Detalleastp.objects.select_related(
        'aseguradoraid', 'tipopolizaid'
    )

    if query:
        terms = query.split()  # Ejemplo: "GNP Vida" → ["GNP", "Vida"]
        q_objects = Q()

        for term in terms:
            # 🔸 Búsqueda por aseguradora
            q_objects |= Q(aseguradoraid__id__icontains=term)
            q_objects |= Q(aseguradoraid__nombre__icontains=term)

            # 🔸 Búsqueda por tipo de póliza
            q_objects |= Q(tipopolizaid__id__icontains=term)
            q_objects |= Q(tipopolizaid__nombre__icontains=term)

        detalles = detalles.filter(q_objects).order_by(
            'aseguradoraid__nombre',
            'tipopolizaid__nombre'
        )
    else:
        detalles = detalles.order_by(
            'aseguradoraid__nombre',
            'tipopolizaid__nombre'
        )

    return render(request, "reportes/AsTP.html", {'detalles': detalles})