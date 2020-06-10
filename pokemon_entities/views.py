import folium

from django.shortcuts import render, get_object_or_404

from .models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, name, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        tooltip=name,
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons_entities = PokemonEntity.objects.all()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for entity in pokemons_entities:
        img = entity.pokemon.image.url if entity.pokemon.image else None

        add_pokemon(
            folium_map,
            entity.lat,
            entity.lon,
            entity.pokemon.title,
            request.build_absolute_uri(img)
        )

    pokemons = Pokemon.objects.all()

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.image.url if pokemon.image else None,
            'title_ru': pokemon.title,
        })

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for pokemon_entity in pokemon.entities.all():
        img = pokemon_entity.pokemon.image.url if pokemon_entity.pokemon.image else None

        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            pokemon_entity.pokemon.title,
            request.build_absolute_uri(img)
        )

    pokemon_dict = {
        "title_ru": pokemon.title,
        "title_en": pokemon.title_en,
        "title_jp": pokemon.title_jp,
        "description": pokemon.description,
        "image": {
            "url": pokemon.image.url if pokemon.image else None
        },
        "previous_evolution": None,
        "next_evolution": None
    }

    if pokemon.previous_evolution:
        pokemon_dict["previous_evolution"] = {
            "pokemon_id": pokemon.previous_evolution.id,
            "title_ru": pokemon.previous_evolution.title,
            "img_url": pokemon.previous_evolution.image.url,
        }

    next_evolution = pokemon.pokemon_next_evolution.first()
    if next_evolution:
        pokemon_dict["next_evolution"] = {
            "pokemon_id": next_evolution.id,
            "title_ru": next_evolution.title,
            "img_url": next_evolution.image.url,
        }

    context = {
        "map": folium_map._repr_html_(),
        "pokemon": pokemon_dict
    }

    return render(request, "pokemon.html", context)
