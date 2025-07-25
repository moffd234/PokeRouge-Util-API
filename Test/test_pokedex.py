from flask import Response


def test_pokedex_success(client, example_pokemon):
    expected_pokemon_info: dict = example_pokemon.to_dict()
    expected_status_code: int = 200

    res: Response = client.get('/pokedex/bulbasaur')
    actual_pokemon_info: dict = res.json
    actual_status_code: int = res.status_code

    assert expected_status_code == actual_status_code
    assert expected_pokemon_info == actual_pokemon_info
