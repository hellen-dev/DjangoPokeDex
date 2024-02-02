from django.urls import path
from .views import get_pokemon_data

# setting urls and urls for pagination
urlpatterns = [
    path('get_pokemon_data/', get_pokemon_data, name='get_pokemon_data'),
    path('get_pokemon_data/<int:page>/', get_pokemon_data, name='get_pokemon_data_paginated')
]