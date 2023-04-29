from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import *

class crear_cliente(ModelForm):
    class Meta:
        model = cliente
        fields = ['cedula', 'nombre', 'apellido', 'direccion', 'telefono', 'correo']

class Registrar_clientes(UserCreationForm):
    #cedula = forms.CharField(max_length=8, primary_key=True)
    #nombre = forms.CharField(max_length=25)
    #apellido = forms.CharField(max_length=25)
    #direccion = forms.CharField(max_length=50)
    #telefono = forms.IntegerField()
    #correo = forms.EmailField()

    class Meta:
        model = cliente
        fields = ['cedula', 'nombre', 'apellido', 'direccion', 'telefono', 'correo']


class inicio_sesion(AuthenticationForm):
    """     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('username') """   
    cedula = forms.CharField(max_length=8)


    class Meta:
        model = cliente
        fields = ('cedula', 'password')

class crear_reservacion(ModelForm):

    class Meta:
        model = reserva
        fields = ['fechaLlegada', 'fechaSalida', 'habitacion', 'cliente']

        widgets = {
            'fechaLlegada': forms.DateInput(attrs={'type': 'date'}),
            'fechaSalida': forms.DateInput(attrs={'type': 'date'})
        }
