from django.db import models



class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    """
    Modelo para representar pedidos de compra y venta.
    """
    TIPO_CHOICES = (
        ('COMPRA', 'Compra'),
        ('VENTA', 'Venta'),
    )

    tipo = models.CharField(max_length=6, choices=TIPO_CHOICES, null=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,null=True)
    cantidad = models.PositiveIntegerField(null=True)
    fecha_pedido = models.DateField(auto_now_add=True)
    fecha_entrega = models.DateField(null=True)

    def _str_(self):
        return f"Pedido de {self.producto.nombre} ({self.cantidad} unidades)"



   

