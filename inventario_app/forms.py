from django import forms
from .models import Proveedor, Producto, Pedido

class ProveedorForm(forms.ModelForm):
     class Meta:
        model = Proveedor
        fields = ['nombre', 'direccion', 'telefono']  
        labels = {
            'nombre': 'Nombre del proveedor',
            'direccion': 'Dirección del proveedor',
            'telefono': 'Teléfono del proveedor'
        }  
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}), 
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),  
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),  
        }  

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'  


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['tipo', 'proveedor', 'producto', 'cantidad', 'fecha_entrega']