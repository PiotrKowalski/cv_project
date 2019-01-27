from django import forms
from .models import Anime
from django.contrib.auth.models import User


class SearchForm(forms.Form):
    model = Anime
    type = (
        ('and', 'AND'),
        ('or', 'OR'),
    )
    genres = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Mystery', 'Mystery'),
        ('Supernatural', 'Supernatural'),
        ('Fantasy', 'Fantasy'),
        ('Sports', 'Sports'),
        ('Romance', 'Romance'),
        ('Slice of Life', 'Slice of Life'),
        ('Horror', 'Horror'),
        ('Psychological', 'Psychological'),
        ('Thriller', 'Thriller'),
        ('Ecchi', 'Ecchi'),
        ('Mech', 'Mech'),
        ('Music', 'Music'),
        ('Mahou Shoujo', 'Mahou Shoujo'),

    )
    type = forms.MultipleChoiceField(choices=type, widget=forms.RadioSelect())
    genres = forms.MultipleChoiceField(choices=genres, widget=forms.CheckboxSelectMultiple())
