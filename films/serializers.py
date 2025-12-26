from rest_framework import serializers
from films.models import DirectorModel, FilmModel, GenresModel


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectorModel
        fields = 'id fio'.split()


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenresModel
        fields = '__all__'


class FilmListSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    genre = serializers.SerializerMethodField()


    class Meta:
        model = FilmModel
        fields = "id title director genre rating is_hit".split()

        # depth = 1 #самый легкий способ

    def get_genre(self, film):
        return film.genre_names


class FilmDetailSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    
    class Meta:
        model = FilmModel
        fields = "__all__"

