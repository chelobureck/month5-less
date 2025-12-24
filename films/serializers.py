from rest_framework import serializers
from films.models import FilmModel


class FilmListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmModel
        fields = "id title rating is_hit".split()


class FilmDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmModel
        fields = "__all__"