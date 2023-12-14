from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from rest_framework.utils import json
from .forms import ProductoForm, UsuarioForm, ImportadorForm, ServicioForm

from django.views.decorators.csrf import csrf_protect


# Create your views here.

def index(request):
    return render(request,'web/index.html')

def login_view(request):
    return render(request, 'web/login.html')

def register_view(request):
    return render(request, 'web/register.html')

def view_admin(request):
    return render(request, 'web/admin.html')

#VISTAS USUARIO

def view_user(request):
    response = requests.get('http://3.228.132.49:8000/usuarios/').json()
    roles = requests.get('http://3.228.132.49:8000/usuarios/roles/').json()
    return render(request, 'web/usuario.html', {'usuarios': response , 'roles': roles})

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
        rol         = 3
        
        data = {'rut': rut, 'nombre': nombre, 'email': email, 'direccion': direccion, 'username': username, 'password': password, 'rol': rol}
        
        headers = {'Content-type': 'application/json', }
        response = requests.post(url, data=json.dumps(data), headers=headers)
        
        return render(request, 'web/index.html', {
            'response': response
        })
        

def usuario_log(request):
    
    usuarios = requests.get('http://3.228.132.49:8000/usuarios/').json()
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
    for usuario in usuarios:
        if usuario.get('username') == username and usuario.get('password') == password:
            id = str(usuario.get('id_usuario'))
            
            
            usuarioN = requests.get('http://3.228.132.49:8000/usuarios/detalle/'+id).json()
            context = {"usuario":usuarioN}
            
            return render(request,'web/index.html', context)
        else:
            context = {"mensaje": '¡Los datos ingresados son incorrectos!'}
            return render(request,'web/login.html', context)
    

def usuario_find(request,pk):
    if pk != "":
        usuario = requests.get('http://3.228.132.49:8000/usuarios/detalle/'+pk).json()
        roles   = requests.get('http://3.228.132.49:8000/usuarios/roles/').json()
        
        context = {"usuario":usuario, "roles":roles}
        return render(request,'web/usuario_find.html', context)
    else:
        mensaje = "El usuario NO existe"
        context = {"mensaje":mensaje}
        return render(request,'web/usuario.html', context)
    

@csrf_protect
def usuario_update(request,pk,rol):
    if pk != "":
        usuario = requests.get('http://3.228.132.49:8000/usuarios/detalle/'+pk).json()
        
        nombre      = usuario.get('nombre')
        username    = usuario.get('username')
        email       = usuario.get('email')
        direccion   = usuario.get('direccion')
        rut         = usuario.get('rut')
        password    = usuario.get('password')
        
        
        url = "http://3.228.132.49:8000/usuarios/actualizar/"+pk
        data = { 'id_usuario': int(pk),'nombre': nombre, 'rut': rut, 'email': email , 'direccion': direccion , 'username': username, 'password': password ,'rol': int(rol) }
        headers = {'Content-type': 'application/json' }
        requests.post(url, data=json.dumps(data), headers=headers)
        
        
        usuarios = requests.get('http://3.228.132.49:8000/usuarios/').json()
        roles = requests.get('http://3.228.132.49:8000/usuarios/roles/').json()
        context = {"usuarios":usuarios , "roles":roles}
        return render(request,'web/usuario.html', context)
    else:
        mensaje = "El usuario NO existe"
        context = {"mensaje":mensaje}
        return render(request,'web/usuario.html', context)

def usuario_del(request,pk):
    if pk != "":
        requests.delete('http://3.228.132.49:8000/usuarios/eliminar/'+pk).json()
        
        usuarios = requests.get('http://3.228.132.49:8000/usuarios/').json()
        return render(request,'web/usuario.html', {'usuarios': usuarios})
    else:
        mensaje = "El usuario NO existe"
        context = {"mensaje":mensaje}
        return render(request,'web/usuario.html', context)


#VISTAS PRODUCTOS

def view_prod(request):
    response = requests.get('http://44.215.197.102:8000/productos/').json()
    categorias = requests.get('http://44.215.197.102:8000/productos/categorias/').json()
    return render(request, 'web/producto.html', {'productos': response , 'categorias': categorias})

def producto_find(request,pk):
    if pk != "":
        producto    = requests.get('http://44.215.197.102:8000/productos/detalle/'+pk).json()
        categorias = requests.get('http://44.215.197.102:8000/productos/categorias/').json()
        
        context = {"producto":producto, "categorias":categorias}
        return render(request,'web/producto_find.html', context)
    else:
        mensaje = "El producto NO existe"
        context = {"mensaje":mensaje}
        return render(request,'web/producto.html', context)

def producto_filter(request,pk):
    if pk != "":
        producto    = requests.get('http://44.215.197.102:8000/productos/detalle/'+pk).json()
        categorias  = requests.get('http://44.215.197.102:8000/productos/categorias/').json()
        context = {"producto":producto, "categorias":categorias}
        return render(request,'web/producto_edit.html', context)
    else:
        mensaje = "El producto NO existe"
        context = {"mensaje":mensaje}
        return render(request,'web/producto.html', context)
    
def producto_del(request,pk):
    if pk != "":
        requests.delete('http://44.215.197.102:8000/productos/eliminar/'+pk).json()
        
        productos = requests.get('http://44.215.197.102:8000/productos/').json()
        return render(request,'web/producto.html', {'productos': productos})
    else:
        mensaje = "El producto NO existe"
        context = {"mensaje":mensaje}
        return render(request,'web/producto.html', context)

@csrf_protect
def producto_update(request,pk):
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        
        categoria   = form.cleaned_data.get("id_categoria")
        nombre      = form.cleaned_data.get("nombre")
        descripcion = form.cleaned_data.get("descripcion")
        precio      = form.cleaned_data.get("precio")
        stock       = form.cleaned_data.get("stock")
        
        data = { 'nombre': nombre, 'descripcion': descripcion, 'stock': stock, 'precio': precio ,'id_categoria': categoria}
        headers = {'Content-type': 'application/json', }
        requests.post('http://44.215.197.102:8000/productos/actualizar/'+pk, data=json.dumps(data), headers=headers)
        
        productoNew = requests.get('http://44.215.197.102:8000/productos/detalle/'+pk).json()
        categorias = requests.get('http://44.215.197.102:8000/productos/categorias/').json()
        context = {"producto":productoNew , "categorias":categorias}
        return render(request,'web/producto_find.html', context)
    else:
        mensaje = "El producto NO existe"
        context = {"mensaje":mensaje}
        return render(request,'web/producto.html', context)

def producto_add(request):
    categorias  = requests.get('http://44.215.197.102:8000/productos/categorias/').json()
    return render(request,'web/producto_add.html', {'categorias': categorias})

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

        data = {'id_categoria': categoria , 'nombre': nombre, 'descripcion': descripcion, 'stock': stock, 'precio': precio }
        headers = {'Content-type': 'application/json', }
        response = requests.post(url, data=json.dumps(data), headers=headers)
        
        productos = requests.get('http://44.215.197.102:8000/productos/').json()
        return render(request, 'web/producto.html', {
            'response': response, 'productos': productos
        })

#VISTAS IMPORTADORES

def view_import(request):
    response = requests.get('http://107.20.132.27:8000/importadores/').json()
    return render(request, 'web/importador.html', {'importadores': response})

def importador_find(request,pk):
    if pk != "":
        importador  = requests.get('http://107.20.132.27:8000/importadores/detalle/'+pk).json()
        
        context = {"importador":importador}
        return render(request,'web/importador_find.html', context)
    else:
        mensaje = "El importador NO existe"
        context = {"mensaje":mensaje}
        return render(request,'web/importador.html', context)

def importador_filter(request,pk):
    if pk != "":
        importador = requests.get('http://107.20.132.27:8000/importadores/detalle/'+pk).json()
        
        context = {"importador":importador}
        return render(request,'web/importador_edit.html', context)
    else:
        mensaje = "El importador NO existe"
        context = {"mensaje":mensaje}
        return render(request,'web/importador.html', context)

@csrf_protect
def importador_update(request,pk):
    form = ImportadorForm(request.POST or None)
    if form.is_valid():
        
        nombre          = form.cleaned_data.get("nombre")
        descripcion     = form.cleaned_data.get("descripcion")
        direccion       = form.cleaned_data.get("direccion")
        representante   = form.cleaned_data.get("representante")
        pais            = form.cleaned_data.get("pais")
        email           = form.cleaned_data.get("email")
        fono            = form.cleaned_data.get("fono")
        
        data = { 'id_importador': int(pk) ,'nombre': nombre, 'descripcion': descripcion, 'direccion': direccion, 'representante': representante, 'pais': pais, 'email': email, 'fono': int(fono)}
        headers = {'Content-type': 'application/json' }
        url = "http://107.20.132.27:8000/importadores/actualizar/"+pk
        
        requests.post(url, data=json.dumps(data), headers=headers)
        
        importadorNew = requests.get('http://107.20.132.27:8000/importadores/detalle/'+pk).json()
        context = {"importador":importadorNew}

        return render(request,'web/importador_find.html', context)
    else:
        mensaje = "El importador NO existe"
        context = {"mensaje":mensaje}
        return render(request,'web/importador.html', context)
    
def importador_add(request):
    return render(request,'web/importador_add.html')

@csrf_protect
def post_importador(request):
    url = "http://107.20.132.27:8000/importadores/crear"
    form = ImportadorForm(request.POST or None)
    if form.is_valid():
        
        nombre          = form.cleaned_data.get("nombre")
        descripcion     = form.cleaned_data.get("descripcion")
        direccion       = form.cleaned_data.get("direccion")
        representante   = form.cleaned_data.get("representante")
        pais            = form.cleaned_data.get("pais")
        email           = form.cleaned_data.get("email")
        fono            = form.cleaned_data.get("fono")
        
        data = {'nombre': nombre, 'descripcion': descripcion, 'direccion': direccion, 'representante': representante, 'pais': pais, 'email': email, 'fono': fono}
        
        headers = {'Content-type': 'application/json', }
        response = requests.post(url, data=json.dumps(data), headers=headers)
        importadores = requests.get('http://107.20.132.27:8000/importadores/').json()
        return render(request, 'web/importador.html', {
            'response': response, 'importadores': importadores
        })

#VISTAS SERVICIOS

def view_serv(request):
    response = requests.get('http://52.202.135.16:8000/servicios/').json()
    areas = requests.get('http://52.202.135.16:8000/servicios/areas/').json()
    return render(request, 'web/servicio.html', {'servicios': response , 'areas': areas})

def servicio_add(request):
    areas = requests.get('http://52.202.135.16:8000/servicios/areas/').json()
    return render(request,'web/servicio_add.html', {'areas': areas})

def importador_del(request,pk):
    if pk != "":
        requests.delete('http://107.20.132.27:8000/importadores/eliminar/'+pk).json()
        
        importadores = requests.get('http://107.20.132.27:8000/importadores/').json()
        return render(request,'web/importador.html', {'importadores': importadores})
    else:
        mensaje = "El importador NO existe"
        context = {"mensaje":mensaje}
        return render(request,'web/importador.html', context)

def servicio_find(request,pk):
    if pk != "":
        servicio = requests.get('http://52.202.135.16:8000/servicios/detalle/'+pk).json()
        areas = requests.get('http://52.202.135.16:8000/servicios/areas/').json()
        
        context = {"servicio":servicio , "areas":areas}
        return render(request,'web/servicio_find.html', context)
    else:
        mensaje = "El servicio NO existe"
        context = {"mensaje":mensaje}
        return render(request,'web/servicio.html', context)

def servicio_del(request,pk):
    if pk != "":
        requests.delete('http://52.202.135.16:8000/servicios/eliminar/'+pk).json()
        
        servicios = requests.get('http://52.202.135.16:8000/servicios/').json()
        areas = requests.get('http://52.202.135.16:8000/servicios/areas/').json()
        return render(request,'web/servicio.html', {'servicios': servicios, 'areas': areas})
    else:
        mensaje = "El servicio NO existe"
        context = {"mensaje":mensaje}
        return render(request,'web/servicio.html', context)
    
def servicio_filter(request,pk):
    if pk != "":
        servicio    = requests.get('http://52.202.135.16:8000/servicios/detalle/'+pk).json()
        areas       = requests.get('http://52.202.135.16:8000/servicios/areas/').json()
        context = {"servicio":servicio, "areas":areas}
        return render(request,'web/servicio_edit.html', context)
    else:
        mensaje = "El servicio NO existe"
        context = {"mensaje":mensaje}
        return render(request,'web/servicio.html', context)
    
@csrf_protect
def servicio_update(request,pk):
    form = ServicioForm(request.POST or None)
    if form.is_valid():
        
        id_area      = form.cleaned_data.get("id_area")
        nombre       = form.cleaned_data.get("nombre")
        descripcion  = form.cleaned_data.get("descripcion")
        valor        = form.cleaned_data.get("valor")
        
        data = {'id_servicio': int(pk), 'id_area': int(id_area), 'nombre': nombre, 'descripcion': descripcion, 'valor': int(valor)}
        headers = {'Content-type': 'application/json'}
        requests.post('http://52.202.135.16:8000/servicios/actualizar/'+pk, data=json.dumps(data), headers=headers)
        
        servicioNew = requests.get('http://52.202.135.16:8000/servicios/detalle/'+pk).json()
        areas = requests.get('http://52.202.135.16:8000/servicios/areas/').json()
        context = {"servicio":servicioNew, "areas":areas}
        return render(request,'web/servicio_find.html', context)
    else:
        mensaje = "El servicio NO existe"
        context = {"mensaje":mensaje}
        return render(request,'web/servicio.html', context)

@csrf_protect
def post_servicio(request):
    url = "http://52.202.135.16:8000/servicios/crear"
    form = ServicioForm(request.POST or None)
    
    if form.is_valid():
        id_area     = form.cleaned_data.get("id_area")
        nombre      = form.cleaned_data.get("nombre")
        descripcion = form.cleaned_data.get("descripcion")
        valor       = form.cleaned_data.get("valor")

        data = {'id_area': id_area , 'nombre': nombre, 'descripcion': descripcion, 'valor': valor }
        
        headers = {'Content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        
        servicios = requests.get('http://52.202.135.16:8000/servicios/').json()
        return render(request, 'web/servicio.html', {
            'response': response, 'servicios': servicios
        })

#VISTAS RESERVAS

def view_reserva(request):
    
    return render(request, 'web/reserva.html')
