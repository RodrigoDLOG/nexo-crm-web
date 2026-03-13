from django.urls import path
from . import views

urlpatterns = [
    path('', views.crear, name='crear'),
    path('<int:cliente_id>/agente', views.crear_agente, name='crear_agente'),
    path('<int:cliente_id>/<int:agente_id>/aseguradora', views.crear_aseguradora, name='crear_aseguradora'),
    path('<int:cliente_id>/<int:agente_id>/<int:aseguradora_id>/tipoPoliza', views.crear_tipoPoliza, name='crear_tipoPoliza'),
    path('<int:cliente_id>/<int:agente_id>/<int:aseguradora_id>/<int:tipoPoliza_id>/pago', views.crear_pago, name='crear_pago'),
]