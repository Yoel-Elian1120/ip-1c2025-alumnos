from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from .layers.services import services
from .layers.persistence import repositories  

# Página de bienvenida
def index_page(request):
    return render(request, 'index.html')

# Registro de usuarios
def register(request):
    if request.method == 'POST':
        nombre = request.POST['username']
        email = request.POST['email']
        contraseña = request.POST['password']

        if not User.objects.filter(username=nombre).exists():
            usuario = User.objects.create_user(username=nombre, email=email, password=contraseña)
            usuario = authenticate(request, username=nombre, password=contraseña)
            login(request, usuario)
            return redirect('home')
        else:
            return HttpResponse("Ese nombre de usuario ya existe.")
    return render(request, 'register.html')

# Página principal con galería
def home(request):
    images = services.getAllImages()
    favourite_list = services.getAllFavourites(request)
    return render(request, 'home.html', {'images': images, 'favourite_list': favourite_list})

# Búsqueda por nombre
def search(request):
    name = request.POST.get('query', '')
    if name:
        images = services.filterByCharacter(name)
        favourite_list = services.getAllFavourites(request)
        return render(request, 'home.html', {'images': images, 'favourite_list': favourite_list})
    return redirect('home')

# Filtrado por tipo
def filter_by_type(request):
    tipo = request.POST.get('type', '')
    if tipo:
        images = services.filterByType(tipo)
        favourite_list = services.getAllFavourites(request)
        return render(request, 'home.html', {'images': images, 'favourite_list': favourite_list})
    return redirect('home')

# Mostrar favoritos del usuario actual
@login_required
def getAllFavouritesByUser(request):
    favourites = services.getAllFavourites(request)
    return render(request, 'favourites.html', {'favourite_list': favourites})

# Guardar favorito
@login_required
def saveFavourite(request):
    services.saveFavourite(request)
    return redirect('home')

# Eliminar favorito
@require_POST
@login_required
def deleteFavourite(request):
    fav_id = request.POST.get("id")
    if fav_id:
        repositories.delete_favourite(fav_id, request.user)
    return redirect("favoritos")

# Cerrar sesión
@login_required
def exit(request):
    logout(request)
    return redirect('home')