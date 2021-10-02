from django.shortcuts import render,redirect
from .models import Persona,Articulo,Cliente,Empleado
from .forms import *
# Create your views here.
#PAGINA INDEX

def index(request,template_name='tienda/index.html'):
    return render(request,template_name)
def navbar(request):
    return render (request,'tienda/navbar.html')
#LISTAS

def persona_lista(request,template_name='tienda/personas.html'):
    personas = Persona.objects.all()
    datos_persona = {"personas":personas}
    return render(request,template_name,datos_persona)

def cliente_lista(request,template_name='tienda/clientes.html'):
    cliente = Cliente.objects.all()
    datos_clente = {"clientes":cliente}
    return render(request,template_name,datos_clente)

def empleado_lista(request,template_name='tienda/empleados.html'):
    empleado = Empleado.objects.all()
    datos_empleado = {"empleados":empleado}
    return render(request,template_name,datos_empleado)



def articulos_lista(request,template_name='tienda/articulos.html'):
    articulo = Articulo.objects.all()
    datos_articulo = {"articulos":articulo}
    return render(request,template_name,datos_articulo)


#FORMS

#Personas

def nueva_persona(request,template_name='tienda/persona_form.html'):
    if request.method == 'POST':
        form = PersonaFrom(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('Persona_listar')
    else:
        form = PersonaFrom()
    dato={"form":form}
    return render(request,template_name,dato)

def modificar_persona(request,pk,template_name='tienda/persona_form.html'):
    persona = Persona.objects.get(num_doc=pk)
    form = PersonaFrom(request.POST or None, instance=persona)
    if form.is_valid():
        form.save(commit=True)
        return redirect("Persona_listar")
    else:
        print(form.errors)
    datos = {'form':form}
    return render(request,template_name,datos)

def eliminar_persona(request,pk,temaplate_name='tienda/persona_confirmar_eliminacion.html'):
    persona = Persona.objects.get(num_doc=pk)
    if request.method=='POST':
        persona.delete()
        return redirect('Persona_listar')
    else:
        dato = {"form":persona}
        return render(request,temaplate_name,dato)

#Persona-Cliente


def nuevo_cliente(request,template_name='tienda/cliente_form.html'):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('Nuevo_Cliente')
    else:
        form = ClienteForm()
    dato={"form":form}
    return render(request,template_name,dato)

def modificar_cliente(request,pk,template_name='tienda/cliente_form.html'):
    cliente = Cliente.objects.get(id=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save(commit=True)
        return redirect("Cliente_listar")
    else:
        print(form.errors)
    datos = {'form':form}
    return render(request,template_name,datos)

def eliminar_cliente(request,pk,temaplate_name='tienda/cliente_confirmar_eliminar.html'):
    cliente = Cliente.objects.get(id=pk)
    if request.method=='POST':
        cliente.delete()
        return redirect('Cliente_listar')
    else:
        dato = {"form":cliente}
        return render(request,temaplate_name,dato)

#Persona-Empleado

def nuevo_empleado(request,template_name='tienda/empleado_form.html'):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('Nuevo_empleado')
    else:
        form = EmpleadoForm()
    dato={"form":form}
    return render(request,template_name,dato)

def modificar_empleado(request,pk,template_name='tienda/empleado_form.html'):
    empleado = Empleado.objects.get(legajo=pk)
    form = EmpleadoForm(request.POST or None, instance=empleado)
    if form.is_valid():
        form.save(commit=True)
        return redirect("Empleado_listar")
    else:
        print(form.errors)
    datos = {'form':form}
    return render(request,template_name,datos)

def eliminar_empleado(request,pk,temaplate_name='tienda/empleado_confirmar_eliminar.html'):
    empleado = Empleado.objects.get(legajo=pk)
    if request.method=='POST':
        empleado.delete()
        return redirect('Empleado_listar')
    else:
        dato = {"form":empleado}
        return render(request,temaplate_name,dato)


#Articulos
def nuevo_articulo(request,template_name='tienda/articulo_form.html'):
    if request.method == 'POST':
        form = ArticulosForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('Nuevo_Articulo')
    else:
        form = ArticulosForm()
    dato={"form":form}
    return render(request,template_name,dato)

#Articulos-Modificar

def modificar_ariculo(request,pk,template_name='tienda/articulo_form.html'):
    articulo = Articulo.objects.get(id = pk)
    form = ArticulosForm(request.POST or None, instance=articulo)
    if form.is_valid():
        form.save(commit=True)
        return redirect("Articulos_lista")
    else:
        print(form.errors)
    datos = {'form':form}
    return render(request,template_name,datos)

#Articulos-Eliminar

def eliminar_articulo(request,pk,temaplate_name='tienda/articulo_confirmar_eliminar.html'):
    articulo = Articulo.objects.get(id=pk)
    if request.method=='POST':
        articulo.delete()
        return redirect('Articulos_lista')
    else:
        dato = {"form":articulo}
        return render(request,temaplate_name,dato)