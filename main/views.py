from .models import *
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .serializers import FilmSerilalizer, PosterSerilalizer, DirectorSerilalizer, GenreSerilalizer


class FilmListViews(ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerilalizer


class FilmCRUDApiViews(RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerilalizer


class GenreListViews(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerilalizer


class GenreCRUDApiViews(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerilalizer


class DirectorListViews(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerilalizer


class DirectorCRUDApiViews(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerilalizer


class PosterListViews(ListCreateAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerilalizer


class PosterCRUDApiViews(RetrieveUpdateDestroyAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerilalizer
