from django.db import models


class Director(models.Model):
    fullname = models.CharField(max_length=150)
    year_of_birth = models.IntegerField()


class Genre(models.Model):
    title = models.CharField(max_length=100)


class Film(models.Model):
    title = models.CharField(max_length=100)
    publish_year = models.IntegerField()
    country = models.CharField(max_length=100)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class Poster(models.Model):
    date = models.DateField()
    films = models.ManyToManyField(Film)
