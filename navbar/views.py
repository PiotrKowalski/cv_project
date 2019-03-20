from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import View
from django.views.generic.edit import FormView
from django.views.generic import UpdateView
from django.views.generic import CreateView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from navbar.forms import GenresForm
from django.views.generic.list import MultipleObjectMixin
from django.views.generic.edit import FormMixin
from django.views.generic.edit import ProcessFormView
from django.views.generic import CreateView
import string
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from .models import NavTitle, Anime, Announcments, Genre


sidebar_anime = Anime.objects.filter(status='RELEASING').order_by('-popularity')[0:25]


class IndexView(ListView):
    """
    Index Page
    Url: https://127.0.0.1:8000
    """
    template_name = 'navbar/index.html'
    queryset = Anime.objects.all()
    context_object_name = 'anime'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['sidebar_anime'] = sidebar_anime
        context['anns'] = Announcments.objects.all()
        context['n'] = range(4)
        context['banners'] = Anime.objects.all().filter(
            status='RELEASING',
            banner_image__isnull=False).order_by('-popularity')[2:8]
        context['active_banner'] = Anime.objects.filter(
            status='RELEASING',
            banner_image__isnull=False).order_by('-popularity')[1]
        context['anime_TVs'] = Anime.objects.filter(media_format='TV', status='RELEASING').order_by('-popularity')[0:8]
        context['anime_movies'] = Anime.objects.filter(media_format='MOVIE').order_by('-start_date')[0:8]
        # And so on for more models
        return context


class AnimeView(DetailView):
    """
    Anime object detail page
    Url: http://127.0.0.1:8000/anime/<int:anime_id>/<slug:anime_url>
    Example Url: http://127.0.0.1:8000/anime/225844/tensei-shitara-slime-datta-ken
    """
    model = Anime
    template_name = 'navbar/anime.html'
    slug_field = 'url'
    slug_url_kwarg = 'anime_url'
    pk_url_kwarg = 'anime_id'
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        anime = self.object
        paginator = Paginator(anime.streaming_episodes_JSON, 13)    # Show 13 episodes per page
        episode_list_page_number = self.request.GET.get('page')

        context = super(AnimeView, self).get_context_data(**kwargs)
        context['sidebar_anime'] = sidebar_anime
        context['episode_list'] = paginator.get_page(episode_list_page_number)
        # And so on for more models
        return context


class DMCAView(View):
    """
    DMCA page
    Url: http://127.0.0.1:8000/DMCA
    """
    def get(self, request, *args, **kwargs):
        return render(request, 'navbar/DMCA.html', context={
            'sidebar_anime': sidebar_anime,
        })


"""
Next 4 views should be merged into one and query should be distinguishable because of the initial letter 
or the type of anime - anime series or movie. 
"""


class AnimeListView(ListView):
    """
    Anime series list page sorted by title and paginated by 23
    Url: http://127.0.0.1:8000/anime-list
    """
    # model = Anime
    template_name = 'navbar/anime_list.html'
    queryset = Anime.objects.all().exclude(media_format='MOVIES', is_adult=True).order_by('title')
    # slug_url_kwarg = 'letter'
    context_object_name = 'anime_list'
    paginate_by = 23

    def get_context_data(self, **kwargs):
        context = super(AnimeListView, self).get_context_data(**kwargs)
        context['sidebar_anime'] = sidebar_anime
        context['letters'] = list(string.ascii_uppercase)
        # context['anime_list'] = paginator.get_page(page)
        # context['anime_list'] = anime
        # And so on for more models
        return context


class AnimeListLetterView(ListView):
    """
    Anime series list page beginning with certain letter, sorted by title and paginated by 23
    Url: http://127.0.0.1:8000/anime-list/<slug:letter>
    Example url: http://127.0.0.1:8000/anime-list/A
    """
    model = Anime
    template_name = 'navbar/anime_list.html'
    context_object_name = 'anime_list'
    paginate_by = 23

    def get_context_data(self, **kwargs):
        context = super(AnimeListLetterView, self).get_context_data(**kwargs)
        context['sidebar_anime'] = sidebar_anime
        context['letters'] = list(string.ascii_uppercase)
        # And so on for more models
        return context

    def get_queryset(self):
        return Anime.objects.filter(title__istartswith=self.kwargs['letter'])


class AnimeMovieListView(ListView):
    """
    Anime TV list page sorted by title and paginated by 23
    Url: http://127.0.0.1:8000/anime-list-movies
    """
    # model = Anime
    template_name = 'navbar/anime_list_movies.html'
    queryset = Anime.objects.filter(media_format='MOVIE').exclude(is_adult=True).order_by('title')
    # slug_url_kwarg = 'letter'
    context_object_name = 'anime_list'
    paginate_by = 23

    def get_context_data(self, **kwargs):
        context = super(AnimeMovieListView, self).get_context_data(**kwargs)
        context['sidebar_anime'] = sidebar_anime
        context['letters'] = list(string.ascii_uppercase)
        # And so on for more models
        return context


class AnimeMovieListLetterView(ListView):
    """
    Anime TV list page beginning with certain letter, sorted by title and paginated by 23
    Url: http://127.0.0.1:8000/anime-list-movies/<slug:letter>
    Example url: http://127.0.0.1:8000/anime-list-movies/A
    """
    model = Anime
    template_name = 'navbar/anime_list_movies.html'
    context_object_name = 'anime_list'
    paginate_by = 23

    def get_context_data(self, **kwargs):
        context = super(AnimeMovieListLetterView, self).get_context_data(**kwargs)
        context['sidebar_anime'] = sidebar_anime
        context['letters'] = list(string.ascii_uppercase)
        # And so on for more models
        return context

    def get_queryset(self):
        return Anime.objects.filter(title__istartswith=self.kwargs['letter'])


class GenresView(ListView, FormMixin, ProcessFormView):
    """
    Getting list of anime using custom form GenresForm and GET method
    Anime are filtered by chosen genres (genres) and OR/AND logical gate (type)
    Anime are sorted by title and paginated by 23
    Url: http://127.0.0.1:8000/genres
    Url: http://127.0.0.1:8000/genres?type=<type>&genres=<genre>
    Example url: http://127.0.0.1:8000/genres?type=and&genres=Fantasy&genres=Sports
    """
    model = Anime
    template_name = 'navbar/genres.html'
    form_class = GenresForm
    context_object_name = 'anime_list'
    success_url = '#'
    paginate_by = 23
    result = None

    def get_context_data(self, **kwargs):
        context = super(GenresView, self).get_context_data(**kwargs)
        # context['anime_list'] = self.result
        # context['form'] = self.form_class()
        # context['form'] = self.get_form()
        context['sidebar_anime'] = sidebar_anime
        context['genre_list'] = Genre.objects.all()
        # And so on for more models
        return context

    def get_queryset(self):
        genres = self.request.GET.getlist('genres')
        type = self.request.GET.get('type')
        if len(genres) > 1:
            new_arr = []
            for key in genres:
                key = '{'+key+'}'
                new_arr.append(key)
            queries = [Q(genres_array__contains=genre) for genre in new_arr]
            query = queries.pop()
            if type == 'or':
                for item in queries:
                    query |= item
            elif type == 'and':
                for item in queries:
                    query &= item
            return Anime.objects.filter(query)
        elif len(genres) == 1:
            return Anime.objects.filter(genres_array__contains=genres)
        else:
            arr = []
            return arr


class SearchView(ListView):
    """
    Getting list of anime using GET method
    Url: http://127.0.0.1:8000/search?anime=<text>
    Example url: http://127.0.0.1:8000/search?anime=mob
    """
    model = Anime
    template_name = 'navbar/search.html'
    context_object_name = 'anime_list'
    paginate_by = 23

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['sidebar_anime'] = sidebar_anime
        # And so on for more models
        return context

    def get_queryset(self):
        query = self.request.GET.get('anime')
        if query:
            return Anime.objects.filter(title__icontains=query).order_by('-popularity')
        else:
            return Anime.objects.all()


class SignUpView(CreateView):
    """
    Sign up page
    Url: http://127.0.0.1:8000/accounts/signup
    """
    template_name = 'navbar/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        context['sidebar_anime'] = sidebar_anime
        # And so on for more models
        return context


class AnimeLoginView(LoginView):
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(AnimeLoginView, self).get_context_data(**kwargs)
        context['sidebar_anime'] = sidebar_anime
        # And so on for more models
        return context


class UserView(DetailView):
    """
    User detail page
    Url: http://127.0.0.1:8000/profile/<slug:username>
    Example url: http://127.0.0.1:8000/profile/Yekoss
    """
    model = User
    context_object_name = "user_page"
    template_name = 'navbar/user_page.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        context = super(UserView, self).get_context_data(**kwargs)
        context['sidebar_anime'] = sidebar_anime
        context['anime'] = Anime.objects.all()
        # And so on for more models
        return context


class UserUpdateView(UserPassesTestMixin, UpdateView):
    """
    User detail update page
    User fields are updated using ModelForm
    This view can be only accessed by authorized user - logged in user's username must be the same as the username slug
    Url: http://127.0.0.1:8000/profile/<slug:username>
    Example url: http://127.0.0.1:8000/profile/Yekoss
    """
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    context_object_name = "user_page"
    template_name = 'navbar/user_update_page.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    # success_url = reverse_lazy('navbar:user')
    redirect_field_name = 'next'

    def test_func(self):
        return self.request.user.username.lower() == self.kwargs['username'].lower()

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('navbar:user', kwargs={'username': self.object.username})

    def get_context_data(self, **kwargs):

        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['sidebar_anime'] = sidebar_anime
        context['anime'] = Anime.objects.all()
        # And so on for more models
        return context
