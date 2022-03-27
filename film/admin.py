from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from . models import Film, GenreFilm
# Register your models here.


class GenreFilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre_id',
                    'published_date', 'daily_rental_rate')
    exclude = ('date_created', )


admin.site.register(GenreFilm, GenreFilmAdmin)
admin.site.register(Film, FilmAdmin)
