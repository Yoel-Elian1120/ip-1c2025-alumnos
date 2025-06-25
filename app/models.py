from django.db import models
from django.conf import settings

class Favourite(models.Model):
    pokemon_id = models.IntegerField()  # ID del Pokémon según PokéAPI
    name = models.CharField(max_length=200)
    height = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    base_experience = models.IntegerField(null=True, blank=True)
    types = models.JSONField(default=list)
    image = models.URLField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'pokemon_id')
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'

    def __str__(self):
        return f"{self.name} - {self.user.username}"