from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes, name='clientes'),
    path('<int:Cliente_id>/', views.cliente_detalle, name='cliente_ver'),
    path('<int:Cliente_id>/editar/', views.cliente_detalle, {'modo': 'editar'}, name='cliente_editar')
]