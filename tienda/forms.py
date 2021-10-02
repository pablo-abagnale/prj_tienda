from django.forms import ModelForm
from django import forms
from .models import Localidad,Persona,Articulo,Cliente,Cargo,Movimiento,Item,Categoria,Empleado

class DateInput(forms.DateInput):
    input_type = 'date'

class LocalidadForm(ModelForm):
    class Meta:
        model = Localidad
        fields = '__all__'

class PersonaFrom(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = { 'num_doc': forms.TextInput(attrs={'type':'number','class':'form-control input'}),
                    'apellido':forms.TextInput(attrs={'class':'form-control input','text-transform':'capitalize','placeholder':'apellido'}),
                    'nombre':forms.TextInput(attrs={'class':'form-control input','text-transform':'capitalize','placeholder':'nombre'}),
                    'telefono':forms.TextInput(attrs={'class':'form-control input','placeholder':'telefono'}),
                    'mails':forms.TextInput(attrs={'class':'form-control input','text-transform':'capitalize','placeholder':'mail@mails.com'}),
                    'fecha_nac':DateInput(format='%Y-%m-%d',attrs= {'class':'form-control input-sm'}),
                    'localidad':forms.Select(attrs={'class':'form-control input'})
        }

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = { 'persona': forms.Select(attrs={'class': 'form-control input'}),
                    'fecha_alta':DateInput(format='%Y-%m-%d',attrs= {'class':'form-control input-sm'}),
                    'Categoria': forms.Select(attrs={'class': 'form-control input'}),
        }

class CargoForm(ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'

class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {'persona': forms.Select(attrs={'class': 'form-control input'}),
                   'legajo': forms.TextInput(attrs={'class':'form-control input','text-transform':'capitalize','placeholder':'Numero de legajo'}),
                   'Cargo':forms.Select(attrs={'class': 'form-control input'}),
                   }

class ArticulosForm(ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'
        widgets ={
            'nombre': forms.TextInput( attrs={'class': 'form-control input', 'text-transform': 'capitalize', 'placeholder': 'nombre'}),
            'marca': forms.TextInput( attrs={'class': 'form-control input', 'text-transform': 'capitalize', 'placeholder': 'marca'}),
            'categoria': forms.TextInput( attrs={'class': 'form-control input', 'text-transform': 'capitalize', 'placeholder': 'categoria'}),
            'descripcion': forms.Textarea( attrs={'class': 'form-control input', 'text-transform': 'capitalize', 'placeholder': 'descripción'}),
            'precio': forms.TextInput(attrs={'type':'number','class':'form-control input'}),
            'stock': forms.TextInput(attrs={'type':'number','class':'form-control input'}),
        }