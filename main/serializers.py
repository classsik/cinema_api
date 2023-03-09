from .models import *
from rest_framework import serializers


class FilmSerilalizer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'


class DirectorSerilalizer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class GenreSerilalizer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class PosterSerilalizer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = '__all__'

