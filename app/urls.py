from django.urls import path
from . import views

urlpatterns = [
    # Autenticación y navegación principal
    path('', views.index_page, name='index-page'),
    path('login/', views.index_page, name='login'),  # vista de login
    path('register/', views.register, name='register'),
    path('exit/', views.exit, name='exit'),

    # Página principal y búsquedas
    path('home/', views.home, name='home'),
    path('buscar/', views.search, name='buscar'),
    path('filter_by_type/', views.filter_by_type, name='filter_by_type'),

    # Favoritos (listar, guardar, borrar)
    path('favourites/', views.getAllFavouritesByUser, name='favoritos'),
    path('favourites/add/', views.saveFavourite, name='agregar-favorito'),
    path('favourites/delete/', views.deleteFavourite, name='borrar-favorito'),
]