# capa DAO de acceso/persistencia de datos.

from sqlite3 import IntegrityError
from app.models import Favourite

def save_favourite(fav):
    try:
        fav = Favourite.objects.create(
            pokemon_id=fav.id,              # ID del Pokémon (no del registro)
            name=fav.name,
            types=fav.types,
            height=fav.height,
            weight=fav.weight,
            base_experience=fav.base,
            image=fav.image,
            user=fav.user
        )
        return fav
    except IntegrityError as e:
        print(f"Error de integridad al guardar el favorito: {e}")
        return None
    except KeyError as e:
        print(f"Error de datos al guardar el favorito: Falta el campo {e}")
        return None

def get_all_favourites(user):
    return list(Favourite.objects.filter(user=user).values(
    'id', 'pokemon_id', 'name', 'height', 'weight', 'types', 'base_experience', 'image'
))
    

def delete_favourite(fav_id, user):
    try:
        favourite = Favourite.objects.get(id=fav_id, user=user)
        favourite.delete()
        return True
    except Favourite.DoesNotExist:
        print(f"El favorito con ID {fav_id} no existe o no pertenece al usuario.")
        return False
    except Exception as e:
        print(f"Error al eliminar el favorito: {e}")
        return False