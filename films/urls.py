from django.urls import path
from films.views import film_list_api_view, film_detail_api_view

urlpatterns = [
    path("", film_list_api_view),
    path("<int:film_id>/", film_detail_api_view),
]
