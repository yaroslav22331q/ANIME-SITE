from django.db import models
from .anime import Anime

def episode_video_path(instance, filename):
    return f"episodes/{instance.anime.slug}/{filename}"

class Episode(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='episodes')
    title = models.CharField(max_length=255)
    number = models.PositiveIntegerField()
    video = models.FileField(upload_to=episode_video_path)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.anime.title} - Episode {self.number}"
