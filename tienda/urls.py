from django.urls import path
from .views import *
urlpatterns = [
    path('', index,name = 'index'),

    #Personas
    path('personas', persona_lista, name='Persona_listar'),
    path('nueva_persona', nueva_persona, name='Nueva_Persona'),
    path('modificar_persona/<int:pk>', modificar_persona, name='modificar_persona'),
    path('eliminar_persona/<int:pk>', eliminar_persona, name='eliminar_persona'),

    #Personas - Clientes

    path('clientes', cliente_lista,name = 'Cliente_listar'),
    path('nuevo_cliente', nuevo_cliente, name='Nuevo_Cliente'),
    path('modificar_cliente/<int:pk>', modificar_cliente, name='modificar_cliente'),
    path('eliminar_cliente/<int:pk>', eliminar_cliente, name='eliminar_cliente'),

    # Personas - Empleados
    path('empleados', empleado_lista,name = 'Empleado_listar'),
    path('nuevo_empleado', nuevo_empleado, name='nuevo_empleado'),
    path('modificar_empleado/<int:pk>', modificar_empleado, name='modificar_empleado'),
    path('eliminar_empleado/<int:pk>', eliminar_empleado, name='eliminar_empleado'),

    #Articulos
    path('articulos', articulos_lista,name = 'Articulos_lista'),
    path('nuevo_articulo', nuevo_articulo,name = 'Nuevo_Articulo'),
    path('modificar_articulo/<int:pk>', modificar_ariculo,name = 'modificar_articulo'),
    path('eliminar_articulo/<int:pk>', eliminar_articulo, name='eliminar_articulo'),

]