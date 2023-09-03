# Proyecto final CoderHouse - Python

#### Comision: 55630
#### Alumno: Mariana Gómez Paradiuk

## Proyecto
Patitas - Adopción de perros y tienda virtual

## Version
1.0

## Descripción

Página web de adopción de perros, complementada con una sección de tienda para apartar al cuidado de los perros en transito.

Un usuario no logueado podrá ver la página de inicio con un resumen de la misión de la página e historias de perros ya adoptados, registrarse, loguearse o ver el about.

Al registrarse accederá al menú completo dandole la posibilidad de agregar, modificar o eliminar elementos de todas las clases utilizadas en el proyecto.

## Clases

Adoptante: (persona que desee adoptar algún perro)
    - nombre
    - apellido
    - email
    - direccion
    - telefono
    - historia
    - perro

    
Articulo: (articulos a la venta)
    - nombre
    - tipo
    - descripcion
    - precio

Avatar: (imágen del usuario)
    - imagen

Local: (Puntos de venta, consulta, adopción)
    - direccion
    - horario_apertura
    - horario_cierre
    - partido
    
Perro: (Animales en adopción)
    - nombre
    - raza
    - edad
    - tamanio
    - color

## Links habilitados

- home
- about
- buscar_articulo/
- buscar/
- adoptante/
- create_adoptante/ 
- update_adoptante/<int:pk>/
- delete_adoptante/<int:pk>/
- articulo/
- create_articulo/
- update_articulo/<int:pk>/
- delete_articulo/<int:pk>/
- local/
- create_local/  
- update_local/<int:pk>/
- delete_local/<int:pk>/
- perro/
- create_perro/   
- update_perro/<int:pk>/
- delete_perro/<int:pk>/
- login/
- logout/
- registro/
- editar_perfil/
- agregar_avatar/

## Superuser
#### usuario: admin
#### contraseña: proyectoMGP 

## Tecnología Utilizada

##### Front-End
- HTML 5
- CSS 3
- Javascript ES6
- Bootstrap 5.2.3

##### Back-End
- Python 3.11.5
- Django 4.2

## Pruebas Realizadas

Ver archivo titulado "Casos_de_test" el cual se encuentra en el presente repositorio.

## Video Demostración

https://youtu.be/GWAO_X8CWgA
