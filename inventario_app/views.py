from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.generic import TemplateView
from .models import Proveedor, Producto, Pedido
from .serializers import ProveedorSerializer, ProductoSerializer, PedidoSerializer
from django.shortcuts import render, redirect
from .forms import ProductoForm, PedidoForm, ProveedorForm
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(data=request.data,
                            context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)  
        return Response({'token': token.key})

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    authentication_classes = [TokenAuthentication]  # Agrega la autenticación de Token
    permission_classes = [IsAuthenticated]  # Agrega el permiso de autenticación

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


#Vistas para la pagina
def index(request):
    return render (request,'index.html')
    # No se necesita configuración de autenticación ni permisos para una vista de plantilla


#vistas para proveedor 
    
def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores})

def detalle_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)   
    return render(request, 'detalle_proveedor.html', {'proveedor': proveedor})

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'crear_proveedor.html', {'form': form})

# Vista para actualizar un proveedor existente
def actualizar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('detalle_proveedor', pk=pk)
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'actualizar_proveedor.html', {'form': form})

# Vista para eliminar un proveeedor existente
def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('lista_proveedores')
    return render(request, 'eliminar_proveedor.html', {'proveedor': proveedor})

#vistas producto

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})


def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)  # Obtener el producto con el ID proporcionado
    return render(request, 'detalle_producto.html', {'producto': producto})


def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})

# Vista para actualizar un producto existente
def actualizar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('detalle_producto', pk=pk)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'actualizar_producto.html', {'form': form})

# Vista para eliminar un producto existente
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})


# vistas pedido

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'lista_pedidos.html', {'pedidos': pedidos})


def detalle_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)  # Obtener el producto con el ID proporcionado
    return render(request, 'detalle_pedido.html', {'pedido': pedido})


def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'crear_pedido.html', {'form': form})

# Vista para actualizar un pedido existente
def actualizar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('detalle_pedido', pk=pk)
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'actualizar_pedido.html', {'form': form})

# Vista para eliminar un pedido existente
def eliminar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        pedido.delete()
        return redirect('lista_pedidos')
    return render(request, 'eliminar_pedido.html', {'pedido': pedido})





