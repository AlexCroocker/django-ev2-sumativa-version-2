from django.contrib import admin
from .models import Cliente, Atencion

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nombre', 'rut', 'correo_electronico', 'telefono', 'monto_costo_formateado')
    search_fields = ('nombre', 'rut', 'correo_electronico', 'telefono')

    @admin.display(description='Monto costo', ordering='monto_costo')
    def monto_costo_formateado(self, obj):
        return obj.formato_clp()

class AtencionAdmin(admin.ModelAdmin):
    list_display = ('id_atencion', 'cliente', 'fecha', 'hora', 'descripcion', 'monto_costo_formateado')
    search_fields = ('cliente__nombre', 'fecha', 'hora', 'descripcion')

    @admin.display(description='Monto costo', ordering='monto_costo')
    def monto_costo_formateado(self, obj):
        return obj.formato_clp()

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Atencion, AtencionAdmin)
