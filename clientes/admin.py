from django.contrib import admin
from .models import Cliente, Generocliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'modificado')
    list_display = ('id', 'nombre', 'appaterno', 'apmaterno', 'celular', 'correo', 'ciudad', 'creado')
    search_fields = ('id', 'nombre', 'appaterno', 'apmaterno', 'rfc', 'curp', 'celular', 'telefono', 'correo', 'codigopostal', 'pais', 'estado', 'municipio', 'ciudad', 'colonia', 'calle', 'numcasa', 'creado')
    list_filter = ('generoid', 'pais', 'estado', 'municipio', 'creado', 'modificado')
    ordering = ('nombre', 'appaterno', 'apmaterno')
    date_hierarchy = 'creado'
    list_per_page = 30

@admin.register(Generocliente)
class GeneroclienteAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'modificado')
    list_display = ('id', 'genero', 'creado')
    ordering = ('genero',)