from django.db import models
from datetime import datetime

# Create your models here.


class Localidad(models.Model):
    nombre = models.CharField(max_length=50)
    cp = models.CharField(max_length=15)

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = 'Localidades'

    def __str__(self):
        return self.nombre



class Persona(models.Model):

    num_doc = models.CharField("Nº de documento",max_length=20,primary_key=True)
    apellido = models.CharField(max_length=70)
    nombre = models.CharField("Nombre/s",max_length=70)
    telefono = models.CharField (max_length=11)
    mails = models.CharField(max_length=70)
    fecha_nac = models.DateField("fecha de nacimiento", default=datetime.now)
    localidad = models.ForeignKey(Localidad,null=True,blank= True,on_delete= models.PROTECT,related_name='persona_localidad')

    class Meta:
        ordering = ["apellido","nombre"]

    def __str__(self):
        return '%s, %s, %s' % (self.num_doc,self.apellido,self.nombre)

#CLIENTE
class Categoria(models.Model):
    num_categoria = models.IntegerField("Categoria",default=0,primary_key=True)
    beneficio = models.FloatField(default=0)
    envio_gratis = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.num_categoria)

class Cliente(models.Model):
    persona = models.ForeignKey(Persona,on_delete= models.PROTECT,related_name='cliente_persona')
    fecha_alta = models.DateField("Fecha de alta", default=datetime.now)
    categoria = models.ForeignKey(Categoria,on_delete= models.PROTECT,related_name='Cliente_categoria')

    def __str__(self):
        return '%s, %s, %s ' % (self.persona,self.categoria,self.fecha_alta)

#EMPLEADOS

class Cargo(models.Model):
    nombre_cargo = models.CharField("Cargo",max_length=70,primary_key=True)
    descripción = models.CharField("Descripción",max_length=150,null=True,blank=True)

    def __str__(self):
        return '%s ' % (self.nombre_cargo)
class Empleado(models.Model):
    persona = models.ForeignKey(Persona,on_delete= models.PROTECT,related_name='Empleado_persona')
    legajo = models.IntegerField(null=False)
    cargo = models.ForeignKey(Cargo,on_delete= models.PROTECT,related_name='Cargo_Empleado')
    def __str__(self):
        return '%s, %s, %s ' % (self.persona,self.legajo,self.cargo)

class Articulo(models.Model):
    nombre = models.CharField(max_length=120,null=False)
    marca = models.CharField(max_length=120,null=False)
    categoria = models.CharField(max_length=120,null=False)
    descripción = models.CharField(max_length=300,null=True)
    precio = models.FloatField(null=False)
    stock = models.IntegerField()
    disponible = models.BooleanField(null=True,blank=True)
    imagen = models.CharField(max_length=300,null=True,blank=True)

    class Meta:
        ordering = ["nombre","marca"]

    def __str__(self):
        return '%s, %s,%s' % (self.nombre,self.marca,self.categoria)

class Movimiento(models.Model):
    tipo = models.CharField(max_length=1,null=False)
    fecha = models.DateTimeField(default=datetime.now)
    cliente = models.ForeignKey(Cliente,on_delete= models.PROTECT,related_name='Cliente_Moviento')
    numero = models.CharField(max_length=70)
    estado = models.BooleanField()

    class Meta:
        ordering = ["tipo","fecha","cliente","estado"]

    def __str__(self):
        return '%s, %s,%s' % (self.tipo,self.fecha,self.numero)

class Item(models.Model):
    articulo = models.ForeignKey(Articulo,on_delete= models.PROTECT,related_name='Intem_Articulo')
    movimiento = models.ForeignKey(Movimiento,on_delete= models.PROTECT,related_name='Item_Moviento')
    cantidad = models.IntegerField(default=0)



