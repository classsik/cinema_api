from django.contrib import admin
from django.urls import path

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('films/', views.FilmListViews.as_view()),
    path('films/<int:pk>', views.FilmCRUDApiViews.as_view()),
    path('genres/', views.GenreListViews.as_view()),
    path('genres/<int:pk>', views.GenreCRUDApiViews.as_view()),
    path('directors/', views.DirectorListViews.as_view()),
    path('directors/<int:pk>', views.DirectorCRUDApiViews.as_view()),
    path('posters/', views.PosterListViews.as_view()),
    path('posters/<int:pk>', views.PosterCRUDApiViews.as_view()),
]
