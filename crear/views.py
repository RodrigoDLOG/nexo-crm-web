from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from clientes.models import Cliente
from clientes.forms import ClienteForm
from agentes.models import Agente
from aseguradoras.models import Aseguradora
from polizas.models import Tipopoliza, Formapago, Metodopago, Poliza
from core.models import Detalleastp
from django.db.models import Q

@login_required
def crear(request):
    query = request.GET.get('q')
    clientes = Cliente.objects.all()

    # 🔹 Búsqueda flexible por nombre, apellidos o ID (sin cambios)
    if query:
        terms = query.split()
        q_objects = Q()
        for term in terms:
            q_objects |= Q(id__icontains=term)
            q_objects |= Q(nombre__icontains=term)
            q_objects |= Q(appaterno__icontains=term)
            q_objects |= Q(apmaterno__icontains=term)
        clientes = clientes.filter(q_objects).order_by('nombre', 'appaterno', 'apmaterno')
    else:
        clientes = clientes.order_by('nombre', 'appaterno', 'apmaterno')

    # --- INICIO DE LA CORRECCIÓN ---

    # Esta variable indicará a la plantilla si debe mostrar el formulario de creación por defecto.
    formulario_con_error = False

    # 🔹 Manejo del formulario para crear cliente
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            return redirect('crear_agente', cliente_id=cliente.id)
        else:
            # Si el formulario NO es válido, activamos la bandera.
            # La página se recargará, pero ahora la plantilla sabrá que debe mostrar el formulario con errores.
            formulario_con_error = True
    else:
        # Si la petición es GET, creamos un formulario vacío.
        form = ClienteForm()

    # Pasamos la nueva variable 'formulario_con_error' al contexto.
    return render(request, 'crear/crear_cliente.html', {
        'clientes': clientes,
        'form': form,
        'formulario_con_error': formulario_con_error
    })
    
    # --- FIN DE LA CORRECCIÓN ---


@login_required
def crear_agente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    query = request.GET.get('q')
    agentes = Agente.objects.all()

    # 🔹 Búsqueda flexible por nombre, apellidos o ID
    if query:
        terms = query.split()
        q_objects = Q()
        for term in terms:
            q_objects |= Q(id__icontains=term)
            q_objects |= Q(nombre__icontains=term)
            q_objects |= Q(apellidopaterno__icontains=term)
            q_objects |= Q(apellidomaterno__icontains=term)
        agentes = agentes.filter(q_objects).order_by('nombre', 'apellidopaterno', 'apellidomaterno')
    else:
        agentes = agentes.order_by('nombre', 'apellidopaterno', 'apellidomaterno')

    return render(request, 'crear/crear_agente.html', {
        'agentes': agentes,
        'cliente': cliente
    })


@login_required
def crear_aseguradora(request, cliente_id, agente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    agente = get_object_or_404(Agente, pk=agente_id)
    aseguradoras_relacionadas = Aseguradora.objects.filter(
        detalleagas__agenteid=agente
    ).order_by('nombre')
    aseguradoras = aseguradoras_relacionadas
    return render(request, 'crear/crear_aseguradora.html', {
        'aseguradoras': aseguradoras,
        'agente': agente,
        'cliente': cliente
    })


@login_required
def crear_tipoPoliza(request, cliente_id, agente_id, aseguradora_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    agente = get_object_or_404(Agente, pk=agente_id)
    aseguradora = get_object_or_404(Aseguradora, pk=aseguradora_id)
    tipoPolizas_relacionadas = Tipopoliza.objects.filter(
        detalleastp__aseguradoraid=aseguradora
    ).order_by('nombre')
    tipoPolizas = tipoPolizas_relacionadas
    return render(request, 'crear/crear_tipoPoliza.html', {
        'tipoPolizas': tipoPolizas,
        'aseguradora': aseguradora,
        'agente': agente,
        'cliente': cliente
    })


@login_required
def crear_pago(request, cliente_id, agente_id, aseguradora_id, tipoPoliza_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    agente = get_object_or_404(Agente, pk=agente_id)
    aseguradora = get_object_or_404(Aseguradora, pk=aseguradora_id)
    tipoPoliza = get_object_or_404(Tipopoliza, pk=tipoPoliza_id)
    formasPago = Formapago.objects.all()
    metodosPago = Metodopago.objects.all()
    detalleAsTP = get_object_or_404(Detalleastp, aseguradoraid=aseguradora_id, tipopolizaid=tipoPoliza_id)
    comision = detalleAsTP.comision
    if request.method == 'POST':
        id = request.POST.get('id')
        formapago_id = request.POST.get('formapagoid')
        metodopago_id = request.POST.get('metodopagoid')
        prima_base = Decimal(request.POST.get('prima'))
        fechafin = request.POST.get('fechafin')
        porcentaje = Decimal('1') + (comision / Decimal('100'))
        prima_final = prima_base * porcentaje
        Poliza.objects.create(
            id=id,
            aseguradoraid=aseguradora,
            agenteid=agente,
            clienteid=cliente,
            tipopolizaid=tipoPoliza,
            formapagoid_id=formapago_id,
            metodopagoid_id=metodopago_id,
            prima=prima_final,
            fechafin=fechafin
        )
        return redirect('polizas')
    return render(request, 'crear/crear_pago.html', {
        'cliente': cliente,
        'agente': agente,
        'aseguradora': aseguradora,
        'tipoPoliza': tipoPoliza,
        'formasPago': formasPago,
        'metodosPago': metodosPago,
        'comision': comision,
    })