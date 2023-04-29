from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


# Create your views here.


def home(request):
    return render(request, 'home.html')


""" def signup(request):
    # return HttpResponse('Hola mundo')
    
    variable = 'Me la voy a cojer, algun dia'

    if request.method == 'GET':

        return render(request, 'signup.html', {
            'form_usuario': UserCreationForm
        })
        # print("Enviando Datos")

    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                usuario = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                usuario.save()
                login(request, usuario)
                return redirect('registrar_clientes')

            except IntegrityError:
                return render(request, 'signup.html', {
                    'form_usuario': UserCreationForm, "error": 'Usuario ya existe'
                })

        return render(request, 'signup.html', {
            'form_usuario': UserCreationForm, "error": 'contraseñas no coinciden'
        })


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm})

    else:
        usuario = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        
        
        if usuario is None:
            return render(request, 'signin.html', {'form': AuthenticationForm, 
            "error":'Usuario o contraseña incorrectos'})
        
        else:
            login(request, usuario)
            return redirect('registrar_clientes') """
        
@staff_member_required
@login_required
def admin_home(request):
    return render(request, 'admin_home.html')

class AdminLoginView(LoginView):
    template_name = 'admin_login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('admin_home')

def clientes(request):
    clientes = cliente.objects.all()

    return render(request, 'clientes.html', {'clientes': clientes})



def registrar_clientes(request):

    if request.method == 'POST':
        form = Registrar_clientes(request.POST)
        if form.is_valid():
            #try:
            form.save()
                #messages.success(request, 'El cliente se ha registrado correctamente')
            return redirect('clientes')
            
            #except IntegrityError:
                #messages.success(request, 'El cliente ya existe')

    
    else:
        form = Registrar_clientes()
    return render(request, 'registrar_cliente.html', {'form':form})

        
def iniciar_sesion(request):

    if request.method == 'POST':
        form = inicio_sesion(data=request.POST)
        if form.is_valid():
            cedula = form.cleaned_data.get('cedula')
            password = form.cleaned_data.get('password')
            cliente = authenticate(request, username=cedula, password=password)
            print('se ha iniciado sesion de forma exitosa')
            
            if cliente is not None:
                login(request, cliente)
                return redirect('home')
    
    else:
        form = inicio_sesion()
    
    return render(request, 'login.html', {'form':form})

def reservacion(request):

    if request.method == 'GET':
        return render(request, 'reservacion.html', {'form' : crear_reservacion})
    
    else:
        try:
            form = crear_reservacion(request.POST)
            nueva_reservacion = form.save(commit=False)
            nueva_reservacion.save()
            return redirect('home')
        except ValueError: return render(request, 'reservacion.html',{'error':'Datos invalidos'})
        


def cerrar_sesion(request):
    logout(request)
    return redirect('home')