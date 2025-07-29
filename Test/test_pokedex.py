from flask import Response


def test_pokedex_success(client, example_pokemon):
    example_pokemon = example_pokemon["bulbasaur"]
    expected_pokemon_info: dict = example_pokemon.to_dict()
    expected_status_code: int = 200

    res: Response = client.get('/pokedex/bulbasaur')
    actual_pokemon_info: dict = res.json
    actual_status_code: int = res.status_code

    assert expected_status_code == actual_status_code
    assert expected_pokemon_info == actual_pokemon_info

def test_pokedex_pokemon_not_found(client):
    expected_status_code: int = 404
    expected_response: dict[str, str] = {"message": "Pokemon not found"}

    res = client.get('/pokedex/bulba')
    actual_response: dict[str, str] = res.json
    actual_status_code: int = res.status_code

    assert actual_status_code == expected_status_code
    assert actual_response == expected_response
