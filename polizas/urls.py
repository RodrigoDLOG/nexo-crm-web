from django.urls import path
from . import views

urlpatterns = [
    path('', views.polizas, name='polizas'),
    path('<str:Poliza_id>/', views.poliza_detalle, name='poliza_ver'),
    path('<str:Poliza_id>/editar/', views.poliza_detalle, {'modo': 'editar'}, name='poliza_editar')
]