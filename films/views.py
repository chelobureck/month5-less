from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from films.models import FilmModel
from films.serializers import FilmListSerializer, FilmDetailSerializer


@api_view(['GET'])
def film_list_api_view(request):
    """
    получает фильмы с бд в виде QuerySet
    переформатирует в Serialize
    """
    films = FilmModel.objects.all()

    data = FilmListSerializer(films, many=True).data

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def film_detail_api_view(request, film_id):
    try:
        film = FilmModel.objects.get(id=film_id)
    except FilmModel.DoesNotExist:
        return Response(data={
            'error': 'film hot found!'
        }, status=status.HTTP_404_NOT_FOUND
        )
    
    data = FilmDetailSerializer(film, many=False).data

    return Response(data=data, status=status.HTTP_200_OK)
