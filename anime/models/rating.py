from django.db import models
from django.conf import settings
from .anime import Anime

class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='ratings')
    score = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    class Meta:
        unique_together = ('user', 'anime')

    def __str__(self):
        return f"{self.user} → {self.anime} = {self.score}"
