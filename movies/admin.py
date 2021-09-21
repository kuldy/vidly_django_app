from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

# Register your models here.
from . models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'release_year', 'daily_rate')
    exclude = ('date_created', )


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
