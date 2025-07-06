from django.contrib import admin
from .models.anime import Anime, Genre
from .models.episode import Episode
from .models.favorite import Favorite
from .models.rating import Rating


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('anime', 'title', 'number', 'created_at')


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'anime')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'anime', 'score')
