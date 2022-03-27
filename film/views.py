from http.client import BAD_REQUEST
import re
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Film, GenreFilm
from .serializers import FilmSerializer, GenreFilmSerialize
from film import serializers

# {
#     "title": "Lords of the ring",
#     "number_in_stock": 23,
#     "daily_rental_rate": 8.0,
#     "is_liked": false,
#     "genre_id": 3
# }


@api_view(['GET', 'POST'])
def film_list(request):
    if request.method == 'GET':
        queryset = Film.objects.select_related('genre_id').all()
        serializer = FilmSerializer(queryset, many=True)
        return Response({'movies': serializer.data})
    elif request.method == 'POST':
        serializer = FilmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def film_detail(request, id):
    film = get_object_or_404(Film, pk=id)
    if request.method == 'GET':
        serializer = FilmSerializer(film)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FilmSerializer(film, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view()
def genre_list(request):
    queryset = GenreFilm.objects.all()
    serializer = GenreFilmSerialize(queryset, many=True)
    return Response(serializer.data)


@api_view()
def genre_detail(request, id):
    genre = get_object_or_404(GenreFilm, pk=id)
    serializer = GenreFilmSerialize(genre)
    return Response(serializer.data)
