from django.shortcuts import render, get_object_or_404, redirect
from .models import Anime, Rating
from .forms import RatingForm
from django.db import models

def anime_list(request):
    animes = Anime.objects.all().order_by('-created_at')
    return render(request, 'anime/anime_list.html', {'animes': animes})

def anime_detail(request, slug):
    anime = get_object_or_404(Anime, slug=slug)
    episodes = anime.episodes.all()

    user_rating = None
    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(user=request.user, anime=anime).first()

        if request.method == 'POST':
            form = RatingForm(request.POST)
            if form.is_valid():
                score = form.cleaned_data['score']
                if user_rating:
                    user_rating.score = score
                    user_rating.save()
                else:
                    Rating.objects.create(user=request.user, anime=anime, score=score)
                return redirect('anime_detail', slug=slug)
        else:
            form = RatingForm(initial={'score': user_rating.score if user_rating else None})
    else:
        form = None

    average_rating = anime.ratings.aggregate(models.Avg('score'))['score__avg']

    return render(request, 'anime/anime_detail.html', {
        'anime': anime,
        'episodes': episodes,
        'form': form,
        'average_rating': average_rating,
        'user_rating': user_rating,
    })


from django.shortcuts import render, get_object_or_404
from .models import Anime, Episode

def episode_detail(request, slug, episode_int):
    anime = get_object_or_404(Anime, slug=slug)
    episode = get_object_or_404(Episode, anime=anime, number=episode_int)
    return render(request, 'anime/episode_detail.html', {
        'anime': anime,
        'episode': episode,
    })
