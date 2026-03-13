from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Cliente
from .forms import ClienteForm
from django.db.models import Q

@login_required
def clientes(request):
    query = request.GET.get('q')
    clientes = Cliente.objects.all()

    if query:
        terms = query.split()  # Ejemplo: "Juan Pérez" → ["Juan", "Pérez"]
        q_objects = Q()

        for term in terms:
            q_objects |= Q(id__icontains=term)
            q_objects |= Q(nombre__icontains=term)
            q_objects |= Q(appaterno__icontains=term)
            q_objects |= Q(apmaterno__icontains=term)

        clientes = clientes.filter(q_objects).order_by('nombre', 'appaterno', 'apmaterno')
    else:
        clientes = clientes.order_by('nombre', 'appaterno', 'apmaterno')

    return render(request, "clientes/clientes.html", {'clientes': clientes})

@login_required
def cliente_detalle(request, Cliente_id, modo=None):
    cliente = get_object_or_404(Cliente, id=Cliente_id)

    if request.method == 'GET':
        form = ClienteForm(instance=cliente)
        return render(request, 'clientes/cliente_detalle.html', {
            'cliente': cliente,
            'form': form,
            'modo': modo
        })
    else:
        try:
            form = ClienteForm(request.POST, instance=cliente)
            form.save()
            return redirect('cliente_ver', Cliente_id=Cliente_id)
        except ValueError:
            return render(request, 'clientes/cliente_detalle.html', {
                'cliente': cliente,
                'form': form,
                'modo': 'editar',
                'error': 'Datos inválidos'
            })