from django.urls import path
from . import views


app_name = 'anime'


urlpatterns = [
    path('', views.anime_list, name='anime_list'),
    path('anime/<slug:slug>/', views.anime_detail, name='anime_detail'),
    path('list/<slug:slug>/<int:episode_int>/', views.episode_detail, name='episode_detail'),
]
