from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User


class AdoptanteForm(forms.Form):
    nombre = forms.CharField(label="Nombre/s",max_length=50,required=True)
    apellido = forms.CharField(label="Apellido/s",max_length=50,required=True)
    email = forms.EmailField(label="Email",required=True)
    direccion = forms.CharField(label="Dirección",max_length=50,required=True)
    telefono = forms.IntegerField(label="Teléfono",required=True)
    historia = forms.CharField(label="Contanos sobre vos",max_length=1000,required=True)
    perro = forms.CharField(label="Nombre perrito interesado",max_length=50,required=True)
    
class ArticuloForm(forms.Form):
    nombre = forms.CharField(label="Articulo",max_length=50,required=True)
    tipo = forms.CharField(label="Tipo",max_length=50,required=True)
    descripcion = forms.CharField(label="Descripción",max_length=500,required=True)
    precio = forms.IntegerField(label="Precio",required=True)

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)

class LocalForm(forms.Form):
    direccion = forms.CharField(label="Direccion",max_length=50,required=True)
    horario_apertura = forms.TimeField(label="Horario apertura",required=True)
    horario_cierre = forms.TimeField(label="Horario cierre",required=True)
    partido = forms.CharField(label="Partido",max_length=50,required=True)
    
class PerroForm(forms.Form):
    nombre = forms.CharField(label="Nombre",max_length=50,required=True)
    raza = forms.CharField(label="Raza",max_length=50,required=True)
    edad = forms.IntegerField(label="Edad",required=True)
    tamanio = forms.CharField(label="Tamaño",max_length=50,required=True)
    color = forms.CharField(label="Color",max_length=50,required=True)

class RegistroUsuariosForm(UserCreationForm):      
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput) 
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)   
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)   

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
