from django.contrib import admin
from .models import Detalleagas, Detalleastp

@admin.register(Detalleagas)
class DetalleagasAdmin(admin.ModelAdmin):
    list_display = ('agenteid', 'aseguradoraid')
    search_fields = ('agenteid', 'aseguradoraid')
    list_filter = ('agenteid', 'aseguradoraid')
    ordering = ('agenteid', 'aseguradoraid')
    list_per_page = 30

@admin.register(Detalleastp)
class DetalleastpAdmin(admin.ModelAdmin):
    list_display = ('aseguradoraid', 'tipopolizaid', 'comision')
    search_fields = ('aseguradoraid', 'tipopolizaid')
    list_filter = ('aseguradoraid', 'tipopolizaid')
    ordering = ('aseguradoraid', 'tipopolizaid')
    list_per_page = 30