from django.contrib import admin
from .models import *
# Register your models here.
my_models = [Localidad,Persona,Articulo,Cliente,Empleado]

admin.site.register(my_models)

