from django.urls import path
from . import views

app_name = 'navbar'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),          # Index page

    path('anime-list', views.AnimeListView.as_view(), name='listTV'),       # Anime TV list section
    path('anime-list/<slug:letter>', views.AnimeListLetterView.as_view(), name='listTVLetter'),

    path('anime-list-movies', views.AnimeMovieListView.as_view(), name='listMovie'),        # Anime Movie list section
    path('anime-list-movies/<slug:letter>', views.AnimeMovieListLetterView.as_view(), name='listMovieLetter'),

    path('anime/<slug:anime_url>', views.AnimeView.as_view(), name='anime'),        # Anime Detail Page
    path('anime/<int:anime_id>/<slug:anime_url>', views.AnimeView.as_view(), name='anime'),
    path('anime/<int:anime_id>', views.AnimeView.as_view(), name='anime'),

    path('search', views.SearchView.as_view(), name='search'),       # Search list
    path('genres', views.GenresView.as_view(), name='genres'),       # Genres list

    path('accounts/signup', views.SignUpView.as_view(), name='signup'),  # Sign up

    path('DMCA', views.DMCAView.as_view(), name='DMCA'),    # DMCA page

    path('profile/<slug:username>', views.UserView.as_view(), name='user'),    # User page
    path('profile/<slug:username>/update', views.UserUpdateView.as_view(), name='userUpdate'),    # User Update page
]
