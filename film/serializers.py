from dataclasses import field
from turtle import title
from rest_framework import serializers
from .models import Film, GenreFilm


class GenreFilmSerialize(serializers.ModelSerializer):
    class Meta:
        model = GenreFilm
        fields = ['id', 'name']


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'title', 'name', 'number_in_stock',
                  'daily_rental_rate', 'published_date', 'is_liked',
                  'genre_id']
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # genre_id = serializers.SerializerMethodField(method_name='get_genre_id')
    name = serializers.StringRelatedField(source='genre_id', read_only=True)
    # published_date = serializers.SerializerMethodField(
    #     read_only=True, method_name='get_published_date')

    # def get_genre_id(self, Film):
    #     return Film.genre.id

    # def get_genre_name(self, Film):
    #     return Film.genre_id.name

    # def get_published_date(self, Film):
    #     return Film.release_year
