from django.contrib import admin
from .models import Agente

@admin.register(Agente)
class AgenteAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'modificado')
    list_display = ('id', 'nombre', 'apellidopaterno', 'apellidomaterno', 'creado')
    search_fields = ('id', 'nombre', 'apellidopaterno', 'apellidomaterno')
    list_filter = ('creado', 'modificado')
    ordering = ('nombre', 'apellidopaterno', 'apellidomaterno')
    date_hierarchy = 'creado'
    list_per_page = 30