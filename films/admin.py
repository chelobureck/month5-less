from django.contrib import admin
from films.models import FilmModel

@admin.register(FilmModel)
class FilmModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'rating'] 
    