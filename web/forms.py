from django import forms

class ProductoForm(forms.Form):
    id_categoria= forms.IntegerField()
    nombre      = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=200)
    precio      = forms.IntegerField()
    stock       = forms.IntegerField()

class UsuarioForm(forms.Form):
    nombre      = forms.CharField(max_length=30)
    rut         = forms.CharField(max_length=9)
    email       = forms.CharField(max_length=35)
    direccion   = forms.CharField(max_length=50)
    username    = forms.CharField(max_length=25)
    password    = forms.CharField(max_length=25)
    rol         = forms.IntegerField()
    
class ImportadorForm(forms.Form):
    nombre          = forms.CharField(max_length=30)
    descripcion     = forms.CharField(max_length=200)
    direccion       = forms.CharField(max_length=50)
    representante   = forms.CharField(max_length=30)
    pais            = forms.CharField(max_length=30)
    email           = forms.CharField(max_length=35)
    fono            = forms.IntegerField()
    
class ServicioForm(forms.Form):
    id_area         = forms.IntegerField()
    nombre          = forms.CharField(max_length=30)
    descripcion     = forms.CharField(max_length=200)
    valor           = forms.IntegerField()
    
