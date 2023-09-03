from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home" ),
    path('about/', about, name="about" ),
    

    #__________________ Busqueda dentro de articulos por nombre ________

    path('buscar_articulo/', buscarArticulo, name="buscar_articulo" ),
    path('buscar/', buscar, name="buscar" ),

    #__________________ CRUD Adoptante _________________________________

    path('adoptante/', AdoptanteList.as_view(), name="adoptante" ),
    path('create_adoptante/', AdoptanteCreate.as_view(), name="create_adoptante" ),    
    path('update_adoptante/<int:pk>/', AdoptanteUpdate.as_view(), name="update_adoptante" ),
    path('delete_adoptante/<int:pk>/', AdoptanteDelete.as_view(), name="delete_adoptante" ),

    #__________________ CRUD Articulo __________________________________

    path('articulo/', ArticuloList.as_view(), name="articulo" ),
    path('create_articulo/', ArticuloCreate.as_view(), name="create_articulo" ),    
    path('update_articulo/<int:pk>/', ArticuloUpdate.as_view(), name="update_articulo" ),
    path('delete_articulo/<int:pk>/', ArticuloDelete.as_view(), name="delete_articulo" ),

    #__________________ CRUD Local _____________________________________

    path('local/', LocalList.as_view(), name="local" ),
    path('create_local/', LocalCreate.as_view(), name="create_local" ),    
    path('update_local/<int:pk>/', LocalUpdate.as_view(), name="update_local" ),
    path('delete_local/<int:pk>/', LocalDelete.as_view(), name="delete_local" ),

    #__________________ CRUD Perro ______________________________________

    path('perro/', PerroList.as_view(), name="perro" ),
    path('create_perro/', PerroCreate.as_view(), name="create_perro" ),    
    path('update_perro/<int:pk>/', PerroUpdate.as_view(), name="update_perro" ),
    path('delete_perro/<int:pk>/', PerroDelete.as_view(), name="delete_perro" ),

    #__________________ Login / Logout / Registracion ___________________

    path('login/', login_request, name="login" ),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout" ),
    path('registro/', register, name="registro" ),
    path('editar_perfil/', editarPerfil, name="editar_perfil" ),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar" ),
]