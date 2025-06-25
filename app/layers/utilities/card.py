class Card:
    TYPE_COLOR_MAP = {
        'grass': 'success',
        'fire': 'danger',
        'water': 'primary'
    }

    def __init__(self, name, height, base, weight, image, types, user=None, id=None, pokemon_id=None):
        self.name = name                # Nombre del Pokémon
        self.height = height            # Altura
        self.weight = weight            # Peso
        self.base = base                # Nivel base de experiencia
        self.image = image              # URL de la imagen
        self.types = types or []        # Lista de tipos (por defecto lista vacía)
        self.user = user                # Usuario asociado (opcional)
        self.id = id                    # ID único del favorito en la base
        self.pokemon_id = pokemon_id    # ID original del Pokémon (PokéAPI)

    def get_color_class(self):
        if not self.types:
            return 'warning'
        main_type = self.types[0].lower()
        return self.TYPE_COLOR_MAP.get(main_type, 'warning')

    def __str__(self):
        return (f'name: {self.name}, height: {self.height}, weight: {self.weight}, '
                f'base: {self.base}, image: {self.image}, user: {self.user}, id: {self.id}, pokemon_id: {self.pokemon_id}')

    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        return (self.name, self.height, self.weight, self.id) == \
               (other.name, other.height, other.weight, other.id)

    def __hash__(self):
        return hash((self.name, self.height, self.weight, self.id))