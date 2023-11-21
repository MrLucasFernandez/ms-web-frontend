from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='inicio'),
    path('productos/', views.view_prod, name='prod'),
    path('usuarios/', views.view_user, name='user'),
    path('form/productos', views.post_producto, name='formprod'),
    path('form/usuario', views.post_usuario, name='formuser')
]
