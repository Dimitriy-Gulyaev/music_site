from django.db import models
from enum import Enum


class IterableEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class Origin(IterableEnum):
    STUDIO = 'studio'
    LIVE = 'live'
    COMPILATION = 'compilation'


class ReleaseType(IterableEnum):
    ALBUM = 'album'
    SINGLE = 'single'
    TRACK = 'track'


class Issue(IterableEnum):
    ORIGINAL = 'original'
    REISSUE = 'reissue'
    REMASTER = 'remaster'


class Status(IterableEnum):
    RELEASED = 'released'
    UPCOMING = 'upcoming'


class Release(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField(blank=True, null=True)
    origin = models.CharField(max_length=15, choices=Origin.choices(), blank=True, null=True)
    release_type = models.CharField(max_length=15, choices=ReleaseType.choices(), blank=True, null=True)
    issue = models.CharField(max_length=15, choices=Issue.choices(), blank=True, null=True)
    status = models.CharField(max_length=15, choices=Status.choices(), blank=True, null=True)
    cover = models.ImageField(upload_to='album_covers/', blank=True, null=True)
    artists = models.ManyToManyField('Artist', blank=True)
    genres = models.ManyToManyField('Genre', blank=True)

    def get_artists(self):
        return ', '.join([str(artist) for artist in self.artists.all()])

    def get_genres(self):
        return ', '.join([str(genre) for genre in self.genres.all()])

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=50, unique=True)
    releases = models.ManyToManyField(Release, blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    releases = models.ManyToManyField(Release, blank=True)

    def __str__(self):
        return self.name
