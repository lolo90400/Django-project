from django.contrib import admin
from .models import Proveedor, Producto, Pedido

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['tipo','proveedor','producto', 'cantidad', 'fecha_pedido', 'fecha_entrega']
    list_filter = ['fecha_pedido', 'fecha_entrega', 'tipo','proveedor'] 
    search_fields = ['producto__nombre']


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'proveedor')
    list_filter = ('proveedor','nombre')
    search_fields = ('nombre', 'descripcion', 'proveedor__nombre')


class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono')
    search_fields = ('nombre', 'direccion', 'telefono')

# Registrar los modelos personalizados en el panel de administración
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Pedido, PedidoAdmin)

