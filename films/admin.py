from django.contrib import admin
from films.models import DirectorModel, FilmModel, GenresModel, ReviewModel

@admin.register(FilmModel)
class FilmModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'director', 'rating'] 

@admin.register(GenresModel)
class GenreModelAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(DirectorModel)
class DirectorModelAdmin(admin.ModelAdmin):
    list_display = ['fio', 'brithday']

@admin.register(ReviewModel)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ['film', 'stars']
