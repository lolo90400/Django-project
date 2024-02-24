from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import ( eliminar_proveedor,
                    index, detalle_producto,  
                    lista_pedidos, lista_productos, actualizar_proveedor,
                    crear_proveedor,
                    crear_producto, eliminar_pedido, actualizar_pedido,
                    lista_proveedores, crear_pedido,  
                    eliminar_producto, actualizar_producto, detalle_pedido, detalle_proveedor,ProveedorViewSet,PedidoViewSet,ProductoViewSet)





urlpatterns = [

    # Agregar las URL del enrutador a las URL del proyecto
    

    #URLS para la api 
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/proveedores/', ProveedorViewSet.as_view({'get': 'list', 'post': 'create'}), name='proveedores-list'),
    path('api/proveedores/<int:pk>/', ProveedorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='proveedores-detail'),

    path('api/productos/', ProductoViewSet.as_view({'get': 'list', 'post': 'create'}), name='productos-list'),
    path('api/productos/<int:pk>/', ProductoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='productos-detail'),

    path('api/pedidos/', PedidoViewSet.as_view({'get': 'list', 'post': 'create'}), name='pedidos-list'),
    path('api/pedidos/<int:pk>/', PedidoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='pedidos-detail'),

    
    
    #urls para la pagina
    
    path('', index, name='index'),

    # URLs de renderizado

    path('', index, name='index'),
    path('crear_producto/', crear_producto, name='crear_producto'),
    path('lista_productos/', lista_productos, name='lista_productos'),
    path('detalle_producto/<int:pk>/', detalle_producto, name='detalle_producto'),
    path('detalle_producto/<int:pk>/actualizar/', actualizar_producto, name='actualizar_producto'),
    path('detalle_producto/<int:pk>/eliminar/', eliminar_producto, name='eliminar_producto'),
    
    path('crear_pedido/', crear_pedido, name='crear_pedido'),
    path('lista_pedidos/', lista_pedidos, name='lista_pedidos'),
    path('detalle_pedido/<int:pk>/', detalle_pedido, name='detalle_pedido'),
    path('detalle_pedido/<int:pk>/actualizar/', actualizar_pedido, name='actualizar_pedido'),
    path('detalle_pedido/<int:pk>/eliminar/', eliminar_pedido, name='eliminar_pedido'),
    
    path('crear_proveedor/', crear_proveedor, name='crear_proveedor'),
    path('lista_proveedores/', lista_proveedores, name='lista_proveedores'),
    path('detalle_proveedor/<int:pk>/', detalle_proveedor, name='detalle_proveedor'),
    path('detalle_proveedor/<int:pk>/actualizar/', actualizar_proveedor, name='actualizar_proveedor'),
    path('detalle_proveedor/<int:pk>/eliminar/', eliminar_proveedor, name='eliminar_proveedor'),
]
    
    







