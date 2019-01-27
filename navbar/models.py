from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField

# Create your models here.


class NavTitle(models.Model):
    name = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Anime(models.Model):

    categories = (
        ('FINISHED', 'FINISHED'),
        ('RELEASING', 'RELEASING'),
        ('NOT_YET_RELEASED', 'NOT_YET_RELEASED'),
        ('CANCELLED', 'CANCELLED',)
    )
    types = (
        ('ANIME', 'ANIME'),
        ('MANGA', 'MANGA')
    )
    seasons = (
        ('WINTER', 'WINTER'),
        ('SPRING', 'SPRING'),
        ('SUMMER', 'SUMMER'),
        ('FALL', 'FALL')
    )
    formats = (
        ('TV', 'TV'),
        ('TV_SHORT', 'TV_SHORT'),
        ('MOVIE', 'MOVIE'),
        ('SPECIAL', 'SPECIAL'),
        ('OVA', 'OVA'),
        ('ONA', 'ONA'),
        ('MUSIC', 'MUSIC'),
        ('MANGA', 'MANGA'),
        ('NOVEL', 'NOVEL'),
        ('ONE_SHORT', 'ONE_SHORT')
    )

    id_API = models.IntegerField(null=True)
    title = models.CharField(max_length=200, null=True)
    url = models.SlugField(max_length=200, null=True)
    type = models.CharField(max_length=100, choices=types, null=True)
    description = models.TextField(null=True)
    status = models.CharField(max_length=200, choices=categories, null=True)
    season = models.CharField(max_length=100, choices=seasons, null=True)
    episodes = models.IntegerField(null=True)
    duration = models.IntegerField(null=True)
    genres = models.CharField(max_length=500, null=True)
    genres_array = ArrayField(models.CharField(max_length=200, null=True), size=None, null=True)
    average_score = models.IntegerField(null=True)
    trending = models.IntegerField(null=True)
    popularity = models.IntegerField(null=True)
    streaming_episodes_JSON = JSONField(null=True)
    imageURL = models.CharField(max_length=500, null=True)
    imageURL_medium = models.CharField(max_length=500, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    banner_image = models.CharField(max_length=500, null=True)
    is_adult = models.BooleanField(null=True)
    media_format = models.CharField(max_length=200, choices=formats, null=True)
    def __str__(self):
        return self.title


class Announcments(models.Model):
    name = models.CharField(max_length=200)
    Description = models.CharField(max_length=2000, blank=True)
    text_on_searchbox = models.CharField(max_length=2000, blank=True)
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# class Carousel_anime(models.Model):
#     name = models.CharField(max_length = 200)
#     Description = models.CharField(max_length = 2000, blank=True)
#     image = models.ImageField(upload_to=None,
#                               height_field=290,
#                               width_field=854,
#                               max_length=100,
#                               blank = True)
#     def __str__(self):
#         return self.name
