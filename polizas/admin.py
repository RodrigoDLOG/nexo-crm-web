from django.contrib import admin
from .models import Tipopoliza, Formapago, Metodopago, Poliza

@admin.register(Tipopoliza)
class TipopolizaAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'modificado')
    list_display = ('id', 'nombre', 'creado')
    search_fields = ('id', 'nombre')
    list_filter = ('creado', 'modificado')
    ordering = ('nombre',)
    date_hierarchy = 'creado'
    list_per_page = 30

@admin.register(Formapago)
class FormapagoAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'modificado')
    list_display = ('id', 'forma', 'creado')
    search_fields = ('id', 'forma')
    list_filter = ('creado', 'modificado')
    ordering = ('forma',)
    date_hierarchy = 'creado'
    list_per_page = 30

@admin.register(Metodopago)
class MetodopagoAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'modificado')
    list_display = ('id', 'metodo', 'creado')
    search_fields = ('id', 'metodo')
    list_filter = ('creado', 'modificado')
    ordering = ('metodo',)
    date_hierarchy = 'creado'
    list_per_page = 30

@admin.register(Poliza)
class PolizaAdmin(admin.ModelAdmin):
    readonly_fields = ('fechainicio', 'modificado')
    list_display = ('id', 'tipopolizaid', 'aseguradoraid', 'agenteid', 'clienteid', 'prima', 'formapagoid', 'metodopagoid', 'fechainicio', 'fechafin')
    search_fields = ('id', 'aseguradoraid__nombre', 'agenteid__nombre', 'clienteid__nombre', 'fechainicio', 'fechafin')
    list_filter = ('tipopolizaid__nombre', 'aseguradoraid__nombre', 'formapagoid__forma', 'metodopagoid__metodo', 'fechainicio', 'fechafin')
    ordering = ('tipopolizaid__nombre', 'aseguradoraid', 'agenteid', 'clienteid')
    date_hierarchy = 'fechainicio'
    list_per_page = 30