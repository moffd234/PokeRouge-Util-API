from Application.Models.Pokemon import Pokemon


def test_pokemon_constructor():
    example_pokemon = Pokemon.query.filter_by(name="BULBASAUR").first()
    assert example_pokemon.id is not None
    assert example_pokemon.name == "BULBASAUR"
    assert example_pokemon.generation == 1
    assert example_pokemon.sub_legendary == False
    assert example_pokemon.legendary == False
    assert example_pokemon.mythical == False
    assert example_pokemon.category == "Seed Pokémon"
    assert example_pokemon.type_1 == "GRASS"
    assert example_pokemon.type_2 == "POISON"
    assert example_pokemon.ability_1 == "OVERGROW"
    assert example_pokemon.ability_2 is None
    assert example_pokemon.hidden_ability == "CHLOROPHYLL"
    assert example_pokemon.height == 0.7
    assert example_pokemon.weight == 6.9
    assert example_pokemon.base_total == 318
    assert example_pokemon.base_hp == 45
    assert example_pokemon.base_attack == 49
    assert example_pokemon.base_defense == 49
    assert example_pokemon.base_sp_attack == 65
    assert example_pokemon.base_sp_defense == 65
    assert example_pokemon.base_speed == 45
    assert example_pokemon.catch_rate == 45
    assert example_pokemon.base_friendship == 50
    assert example_pokemon.base_exp == 64
    assert example_pokemon.growth_rate == "MEDIUM_SLOW"
    assert example_pokemon.male_percent == 87.5
    assert example_pokemon.gender_diffs == False

def test_pokemon_to_dict():
    example_pokemon = Pokemon.query.filter_by(name="BULBASAUR").first()
    expected: dict = {
            "id": 1,
            "name": "BULBASAUR",
            "generation": 1,
            "category": "Seed Pokémon",
            "legendary_status": {
                "sub_legendary": False,
                "legendary": False,
                "mythical": False,
            },
            "types": {
                "type_1": "GRASS",
                "type_2": "POISON",
            },
            "abilities": {
                "ability_1": "OVERGROW",
                "ability_2": None,
                "hidden_ability": "CHLOROPHYLL",
            },
            "size": {
                "height": 0.7,
                "weight": 6.9,
            },
            "stats": {
                "total": 318,
                "hp": 45,
                "attack": 49,
                "defense": 49,
                "sp_attack": 65,
                "sp_defense": 65,
                "speed": 45,
            },
            "catch_rate": 45,
            "base_friendship": 50,
            "base_exp": 64,
            "growth_rate": "MEDIUM_SLOW",
            "male_percent": 87.5,
            "gender_diffs": False,
        }
    actual: dict = example_pokemon.to_dict()

    assert actual == expected