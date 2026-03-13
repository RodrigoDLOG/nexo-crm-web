from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Poliza
from .forms import PolizaForm
from django.contrib.auth.decorators import login_required

@login_required
def polizas(request):
    query = request.GET.get('q')
    polizas = Poliza.objects.select_related(
        'clienteid', 'agenteid', 'aseguradoraid', 'tipopolizaid', 'formapagoid', 'metodopagoid'
    )

    if query:
        terms = query.split()  # ["Juan", "Pérez"]
        q_objects = Q()  # Contenedor de OR
        for term in terms:
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
        polizas = polizas.filter(q_objects).order_by(
            'fechafin', 'aseguradoraid__nombre', 'agenteid__nombre', 'agenteid__apellidopaterno',
            'agenteid__apellidomaterno', 'clienteid__nombre', 'clienteid__appaterno', 'clienteid__apmaterno'
        )
    else:
        polizas = polizas.all().order_by(
            'fechafin', 'aseguradoraid__nombre', 'agenteid__nombre', 'agenteid__apellidopaterno',
            'agenteid__apellidomaterno', 'clienteid__nombre', 'clienteid__appaterno', 'clienteid__apmaterno'
        )

    return render(request, "polizas/polizas.html", {'polizas':polizas})

@login_required
def poliza_detalle(request, Poliza_id, modo=None):
    poliza = get_object_or_404(Poliza, id=Poliza_id)

    if request.method == 'GET':
        form = PolizaForm(instance=poliza)
        return render(request, 'polizas/poliza_detalle.html', {
            'poliza': poliza,
            'form': form,
            'modo': modo
        })    
    else:
        try:
            form = PolizaForm(request.POST, instance=poliza)
            form.save()
            return redirect('poliza_ver', Poliza_id=Poliza_id)
        except ValueError:
            return render(request, 'polizas/poliza_detalle.html', {
                'poliza': poliza,
                'form': form,
                'modo': 'editar',
                'error': 'Datos inválidos'
            })