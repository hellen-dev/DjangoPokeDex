from django.urls import path
from .views import get_pokemon_data, get_pokemon_by_weight, get_grass_pokemon

# Setting urls and pagination
urlpatterns = [
    path('get_pokemon_data/', get_pokemon_data, name='get_pokemon_data'),
    path('get_pokemon_data/<int:page>/', get_pokemon_data, name='get_pokemon_data_paginated'),

    path('get_pokemon_by_weight/', get_pokemon_by_weight, name='get_pokemon_by_weight'),
    path('get_pokemon_by_weight/<int:page>/', get_pokemon_by_weight, name='get_pokemon_by_weight_paginated'),

    path('get_grass_pokemon/', get_grass_pokemon, name='get_grass_pokemon'),
    path('get_grass_pokemon/<int:page>/', get_grass_pokemon, name='get_grass_pokemon_paginated'),
]