from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from rest_framework.utils import json
from .forms import ProductoForm
from .forms import UsuarioForm
from django.views.decorators.csrf import csrf_protect


# Create your views here.

def index(request):
    return render(request,'web/index.html')

def view_prod(request):
    response = requests.get('http://44.215.197.102:8000/productos/').json()
    return render(request, 'web/producto.html', {
        'response': response
    })

def view_user(request):
    response = requests.get('http://3.228.132.49:8000/usuarios/').json()
    return render(request, 'web/usuario.html', {
        'response': response
    })


@csrf_protect
def post_producto(request):
    url = "http://44.215.197.102:8000/productos/crear"
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        categoria   = form.cleaned_data.get("id_categoria")
        nombre      = form.cleaned_data.get("nombre")
        descripcion = form.cleaned_data.get("descripcion")
        precio      = form.cleaned_data.get("precio")
        stock       = form.cleaned_data.get("stock")

        print(categoria)
        print(nombre)
        print(descripcion)
        print(precio)
        print(stock)
        data = {'id_categoria': categoria , 'nombre': nombre, 'descripcion': descripcion, 'stock': stock, 'precio': precio }
        headers = {'Content-type': 'application/json', }
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return render(request, 'web/form.html', {
            'response': response
        })

@csrf_protect
def post_usuario(request):
    url = "http://3.228.132.49:8000/usuarios/crear"
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        rut         = form.cleaned_data.get("rut")
        nombre      = form.cleaned_data.get("nombre")
        email       = form.cleaned_data.get("email")
        direccion   = form.cleaned_data.get("direccion")
        username    = form.cleaned_data.get("username")
        password    = form.cleaned_data.get("password")
        rol         = form.cleaned_data.get("rol")
        
        data = {'rut': rut, 'nombre': nombre, 'email': email, 'direccion': direccion, 'username': username, 'password': password, 'rol': rol}
        
        headers = {'Content-type': 'application/json', }
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return render(request, 'web/form.html', {
            'response': response
        })
