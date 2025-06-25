# capa de servicio / lógica de negocio

from ..transport import transport
from ...config import config
from ..persistence import repositories
from ..utilities import translator
from django.contrib.auth import get_user

# Obtener todos los Pokémon desde la API PokéAPI y convertirlos a Card
def getAllImages():
    raw_images = transport.get_all_data()
    cards = [translator.to_card(image) for image in raw_images]
    return cards

# Buscador por nombre (parcial, insensible a mayúsculas)
def filterByCharacter(name):
    return [card for card in getAllImages() if name.lower() in card.name.lower()]

# Buscador por tipo (fire, water, grass, etc.)
def filterByType(type_filter):
    return [card for card in getAllImages() if any(type_filter.lower() == t.lower() for t in card.types)]

# Guardar un favorito (asociado al usuario logueado)
def saveFavourite(request):
    fav = translator.fromRequestIntoCard(request)
    fav.user = get_user(request)
    return repositories.save_favourite(fav)

# Listar favoritos de un usuario (convertidos a Card)
def getAllFavourites(request):
    if not request.user.is_authenticated:
        return []
    
    user = get_user(request)
    favourite_list = repositories.get_all_favourites(user)
    return [translator.fromFavouriteToCard(fav) for fav in favourite_list]

# Eliminar favorito (solo si pertenece al usuario logueado)
def deleteFavourite(request):
    fav_id = request.POST.get('id')
    user = get_user(request)
    return repositories.delete_favourite(fav_id, user)

# Obtener URL de ícono por tipo de Pokémon (ej: fire, grass)
def get_type_icon_url_by_name(type_name):
    type_id = config.TYPE_ID_MAP.get(type_name.lower())
    if not type_id:
        return None
    return transport.get_type_icon_url_by_id(type_id)