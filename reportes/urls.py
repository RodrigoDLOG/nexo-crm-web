from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='reportes'),
    path('polizas/', views.reporte_polizas, name='reporte_polizas'),
    path('agentes_aseguradoras/', views.reporte_AgAs, name='reporte_AgAs'),
    path('aseguradoras_tipos/', views.reporte_AsTP, name='reporte_AsTP'),
]