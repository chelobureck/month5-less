from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from films.models import FilmModel
from films.serializers import FilmListSerializer, FilmDetailSerializer


@api_view(['GET', 'POST'])
def film_list_api_view(request):
    """
    получает фильмы с бд в виде QuerySet
    переформатирует в Serialize
    """
    if request.method == 'GET':
        films = FilmModel.objects.select_related('director').prefetch_related('reviews', 'genre').all()

        data = FilmListSerializer(films, many=True).data

        return Response(data=data, status=status.HTTP_200_OK)
    if request.method == "POST":
        print(request.data)
        title = request.data.get('title')
        text = request.data.get('text')
        relaese_year = request.data.get('relaese_year')
        rating = request.data.get('rating')
        is_hit = request.data.get('is_hit')
        director_id = request.data.get("director_id")
        genres = request.data.get("genres")

        film = FilmModel.objects.create(
            title=title,
            text=text,
            relaese_year=relaese_year,
            rating=rating,
            is_hit=is_hit,
            director_id=director_id
        )
        film.genre.set(genres)

        return Response(status=status.HTTP_201_CREATED, data=FilmDetailSerializer(film).data)


@api_view(['GET', 'PUT', 'DELETE'])
def film_detail_api_view(request, film_id):
    try:
        film = FilmModel.objects.get(id=film_id)
    except FilmModel.DoesNotExist:
        return Response(data={
            'error': 'film hot found!'
        }, status=status.HTTP_404_NOT_FOUND
        )
    
    if request.method == 'GET':
        data = FilmDetailSerializer(film, many=False).data

        return Response(data=data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        film.title = request.data.get("title")
        film.text = request.data.get("text")
        film.relaese_year = request.data.get("relaese_year")
        film.rating = request.data.get("rating")
        film.is_hit = request.data.get("is_hit")
        film.director_id = request.data.get("director_id") #type: ignore
        film.genre.set(request.data.get("genres"))
        film.save()
        return Response(status=status.HTTP_201_CREATED, data=FilmDetailSerializer(film).data)
    
    if request.method == 'DELETE':
        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)