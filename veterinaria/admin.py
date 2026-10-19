from django.contrib import admin
from .models import Cliente, Atencion

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nombre', 'rut', 'correo_electronico', 'telefono', 'monto_costo')
    search_fields = ('nombre', 'rut', 'correo_electronico', 'telefono')

class AtencionAdmin(admin.ModelAdmin):
    list_display = ('id_atencion', 'cliente', 'fecha', 'hora', 'descripcion', 'monto_costo')
    search_fields = ('cliente__nombre', 'fecha', 'hora', 'descripcion')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Atencion, AtencionAdmin)
