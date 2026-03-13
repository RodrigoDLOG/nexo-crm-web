from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.iniciar_sesion, name='login'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
]