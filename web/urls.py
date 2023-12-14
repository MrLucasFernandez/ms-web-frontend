from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='inicio'),  
    path('index/',views.index,name='index'),
    path('login/',views.login_view,name='login'),
    path('register/',views.register_view,name='register'),
    
    path('administration/', views.view_admin, name='admin'),
    
    path('usuarios/', views.view_user, name='usuario'),
    path("usuario_find/<str:pk>", views.usuario_find, name="usuario_find"),
    path("usuario_update/<str:pk>/<str:rol>", views.usuario_update, name="usuario_update"),
    path("usuario_del/<str:pk>", views.usuario_del, name="usuario_del"),
    path("usuario_log/", views.usuario_log, name="usuario_log"),
    
    path('productos/', views.view_prod, name='producto'),
    path("producto_find/<str:pk>", views.producto_find, name="producto_find"),
    path("producto_filter/<str:pk>", views.producto_filter, name="producto_filter"),
    path("producto_del/<str:pk>", views.producto_del, name="producto_del"),
    path("producto_add/", views.producto_add, name="producto_add"),
    path("producto_update/<str:pk>", views.producto_update, name="producto_update"),
    
    path('importadores/', views.view_import, name='importador'),
    path("importador_find/<str:pk>", views.importador_find, name="importador_find"),
    path("importador_filter/<str:pk>", views.importador_filter, name="importador_filter"),
    path("importador_add/", views.importador_add, name="importador_add"),
    path("importador_del/<str:pk>", views.importador_del, name="importador_del"),
    path("importador_update/<str:pk>", views.importador_update, name="importador_update"),
    
    path('servicios/', views.view_serv, name='servicio'),
    path("servicio_find/<str:pk>", views.servicio_find, name="servicio_find"),
    path("servicio_filter/<str:pk>", views.servicio_filter, name="servicio_filter"),
    path("servicio_del/<str:pk>", views.servicio_del, name="servicio_del"),
    path("servicio_add/", views.servicio_add, name="servicio_add"),
    path("servicio_update/<str:pk>", views.servicio_update, name="servicio_update"),
    
    path('reservas/', views.view_reserva, name='reserva'),
    
    path('form/productos', views.post_producto, name='formprod'),
    path('form/usuario', views.post_usuario, name='formuser'),
    path('form/importador', views.post_importador, name='formimport'),
    path('form/servicio', views.post_servicio, name='formserv'),
]
