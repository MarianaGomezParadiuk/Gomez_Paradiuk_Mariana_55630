from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import *
from .forms import *

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth       import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "aplicacion/home.html")

def about(request):
    return render(request, "aplicacion/about.html")

#__________________ Busqueda dentro de articulos por nombre ________

@login_required
def buscarArticulo(request):
    return render(request, "aplicacion/buscar_articulo.html")

@login_required
def buscar(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        articulos = Articulo.objects.filter(nombre__icontains=patron)
        contexto = {"articulos": articulos, 'titulo': f'Articulos que tiene como patron "{patron}"'}
        return render(request, "aplicacion/articulo.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")

#___________________________________________________________________

#__________________ CRUD Adoptante _________________________________

class AdoptanteList(LoginRequiredMixin, ListView):
    model = Adoptante

class AdoptanteCreate(LoginRequiredMixin, CreateView):
    model = Adoptante
    fields = ['nombre', 'apellido', 'email', 'direccion', 'telefono', 'historia', 'perro']
    success_url = reverse_lazy('adoptante')

class AdoptanteUpdate(LoginRequiredMixin, UpdateView):
    model = Adoptante
    fields = ['nombre', 'apellido', 'email', 'direccion', 'telefono', 'historia', 'perro']
    success_url = reverse_lazy('adoptante')

class AdoptanteDelete(LoginRequiredMixin, DeleteView):
    model = Adoptante
    success_url = reverse_lazy('adoptante')

#___________________________________________________________________

#__________________ CRUD Articulo __________________________________

class ArticuloList(LoginRequiredMixin, ListView):
    model = Articulo

class ArticuloCreate(LoginRequiredMixin, CreateView):
    model = Articulo
    fields = ['nombre', 'tipo', 'descripcion', 'precio']
    success_url = reverse_lazy('articulo')

class ArticuloUpdate(LoginRequiredMixin, UpdateView):
    model = Articulo
    fields = ['nombre', 'tipo', 'descripcion', 'precio']
    success_url = reverse_lazy('articulo')

class ArticuloDelete(LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = reverse_lazy('articulo')

#___________________________________________________________________


#__________________ CRUD Local _____________________________________

class LocalList(LoginRequiredMixin, ListView):
    model = Local

class LocalCreate(LoginRequiredMixin, CreateView):
    model = Local
    fields = ['direccion', 'partido', 'horario_apertura', 'horario_cierre']
    success_url = reverse_lazy('local')

class LocalUpdate(LoginRequiredMixin, UpdateView):
    model = Local
    fields = ['direccion', 'partido', 'horario_apertura', 'horario_cierre']
    success_url = reverse_lazy('local')

class LocalDelete(LoginRequiredMixin, DeleteView):
    model = Local
    success_url = reverse_lazy('local')

#___________________________________________________________________


#__________________ CRUD Perro _____________________________________

class PerroList(LoginRequiredMixin, ListView):
    model = Perro

class PerroCreate(LoginRequiredMixin, CreateView):
    model = Perro
    fields = ['nombre', 'raza', 'edad', 'tamanio', 'color']
    success_url = reverse_lazy('perro')

class PerroUpdate(LoginRequiredMixin, UpdateView):
    model = Perro
    fields = ['nombre', 'raza', 'edad', 'tamanio', 'color']
    success_url = reverse_lazy('perro')

class PerroDelete(LoginRequiredMixin, DeleteView):
    model = Perro
    success_url = reverse_lazy('perro')

#___________________________________________________________________


#__________________ Login / Logout / Registracion __________________

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)

                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.svg"
                finally:
                    request.session["avatar"] = avatar

                return render(request, "aplicacion/home.html", {'mensaje': f'Bienvenido a nuestro sitio {usuario}'})
            else:
                return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})
        else:
            return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})

    miForm =   AuthenticationForm()      

    return render(request, "aplicacion/login.html", {"form":miForm})    

def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "aplicacion/home.html")
    else:
        miForm =   RegistroUsuariosForm()      
    return render(request, "aplicacion/registro.html", {"form":miForm}) 

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request,"aplicacion/home.html")
        else:
            return render(request,"aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario.username})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)

            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request,"aplicacion/home.html")
    else:
        form = AvatarForm()
    return render(request, "aplicacion/agregarAvatar.html", {'form': form })

#___________________________________________________________________