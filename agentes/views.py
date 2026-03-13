from django.shortcuts import render
from .models import Agente
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def agentes(request):
    query = request.GET.get('q')
    agentes = Agente.objects.all()

    if query:
        terms = query.split()  # Divide "Juan Pérez" en ["Juan", "Pérez"]
        q_objects = Q()

        for term in terms:
            q_objects |= Q(nombre__icontains=term)
            q_objects |= Q(apellidopaterno__icontains=term)
            q_objects |= Q(apellidomaterno__icontains=term)
            q_objects |= Q(id__icontains=term)

        agentes = agentes.filter(q_objects).order_by('nombre', 'apellidopaterno', 'apellidomaterno')
    else:
        agentes = agentes.order_by('nombre', 'apellidopaterno', 'apellidomaterno')

    return render(request, "agentes/agentes.html", {'agentes': agentes})