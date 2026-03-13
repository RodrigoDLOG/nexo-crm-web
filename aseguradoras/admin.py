from django.contrib import admin
from .models import Aseguradora

@admin.register(Aseguradora)
class AseguradoraAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'modificado')
    list_display = ('id', 'nombre', 'creado')
    search_fields = ('id', 'nombre')
    list_filter = ('creado', 'modificado')
    ordering = ('nombre',)
    date_hierarchy = 'creado'
    list_per_page = 30