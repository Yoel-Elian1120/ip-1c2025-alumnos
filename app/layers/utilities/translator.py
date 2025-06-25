import ast
from app.layers.utilities.card import Card

# ✅ Conversión desde la PokéAPI → Card
def to_card(raw_data):
    return Card(
        id=raw_data.get('id'),
        name=raw_data.get('name'),
        height=raw_data.get('height'),
        weight=raw_data.get('weight'),
        base=raw_data.get('base_experience'),
        image=safe_get(raw_data, 'sprites', 'other', 'official-artwork', 'front_default'),
        types=[t.get('type', {}).get('name', '') for t in raw_data.get('types', [])]
    )

# ✅ Conversión desde request.POST (formulario) → Card
def fromTemplateIntoCard(request):
    try:
        poke_id = int(request.POST.get("id"))
    except (TypeError, ValueError):
        raise ValueError("Falta o no es válido el ID del Pokémon")

    types_raw = request.POST.get("types", "[]")
    try:
        types = ast.literal_eval(types_raw) if isinstance(types_raw, str) else types_raw
    except:
        types = []

    return Card(
        id=poke_id,
        name=request.POST.get("name"),
        height=request.POST.get("height"),
        weight=request.POST.get("weight"),
        base=request.POST.get("base"),
        image=request.POST.get("image"),
        types=types
    )

# ✅ Conversión desde un diccionario de base de datos → Card
def fromRepositoryIntoCard(repo_dict):
    types_list = ast.literal_eval(repo_dict.get('types', '[]')) if isinstance(repo_dict.get('types'), str) else repo_dict.get('types', [])
    return Card(
        id=repo_dict.get('id'),  # ← ESTE es el ID de Favourite, clave para borrar
        name=repo_dict.get('name'),
        height=repo_dict.get('height'),
        weight=repo_dict.get('weight'),
        base=repo_dict.get('base_experience'),
        image=repo_dict.get('image'),
        types=types_list,
        pokemon_id=repo_dict.get('pokemon_id')  # ← Podés guardar también esto si lo necesitás
    )

# ⚙️ Utilidad segura para obtener claves anidadas
def safe_get(dic, *keys):
    for key in keys:
        if not isinstance(dic, dict):
            return None
        dic = dic.get(key, {})
    return dic if dic else None

# 🔁 Aliases para compatibilidad
fromRequestIntoCard = fromTemplateIntoCard
fromFavouriteToCard = fromRepositoryIntoCard