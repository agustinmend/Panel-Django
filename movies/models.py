import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class Meta:
        abstract = True

class Genre(UUIDMixin, TimeStampedMixin):
    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    class Meta:
        db_table = "content\".\"genre"
        verbose_name = 'Género'
        verbose_name_plural = 'Genéros'
    
    def __str__(self):
        return self.name
    
class FilmWorkType(models.TextChoices):
    MOVIE = 'movie', 'Movie'
    TV_SHOW = 'tv_show', 'TV Show'
    
class FilmWork(UUIDMixin, TimeStampedMixin):
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    creation_date = models.DateField(_('creation date'), blank=True, null=True)
    rating = models.FloatField(_('rating'), blank=True, validators=[MinValueValidator(0), MaxValueValidator(100)])
    type = models.CharField(_('type'), max_length=50, choices=FilmWorkType.choices)
    genres = models.ManyToManyField(Genre, through='GenreFilmWork')
    class Meta:
        db_table = "content\".\"film_work"
        verbose_name = 'Pelicula'
        verbose_name_plural = 'Peliculas'
    def __str__(self):
        return self.title
    
class GenreFilmWork(UUIDMixin):
    film_work = models.ForeignKey('FilmWork', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "content\".\"genre_film_work"

class Person(UUIDMixin, TimeStampedMixin):
    full_name = models.CharField(_('full_name'), max_length=255)
    class Meta:
        db_table = "content\".\"person"
        verbose_name = "Persona"
        verbose_name_plural = "Personas" 
    def __str__(self):
        return self.full_name

class PersonFilmWork(UUIDMixin):
    film_work = models.ForeignKey('FilmWork', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    role = models.TextField(_('role'), null=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "content\".\"person_film_work"