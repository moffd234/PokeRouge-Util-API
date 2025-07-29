from unittest.mock import patch

from flask import Response


def test_incomplete_weakness_route(client, example_pokemon):
    expected_response: None = None
    actual: Response = client.get('/weaknesses/')

    assert actual.json == expected_response
    assert actual.status_code == 404


def test_get_weakness_summary_pokemon_empty_str(client, example_pokemon):
    expected_response: None = None
    actual: Response = client.get('/weaknesses/summary/')

    assert actual.json == expected_response
    assert actual.status_code == 404


def test_get_weakness_summary(client, example_pokemon):
    expected_summary: dict = {
        "offensive_weaknesses": {"grass": sorted(["flying", "poison", "bug", "steel", "fire", "grass", "dragon"]),
                                 "poison": sorted(["poison", "ground", "rock", "ghost"])},
        "defensive_weaknesses": sorted(["flying", "fire", "psychic", "ice"]),
        "immunities": [],
        "immune_defenders": {"grass": [], "poison": ["steel"]},
    }

    actual: Response = client.get('/weaknesses/summary/bulbasaur')

    assert expected_summary == actual.json
    assert actual.status_code == 200


def test_get_weakness_summary_mixed_case(client, example_pokemon):
    expected_summary: dict = {
        "offensive_weaknesses": {"grass": sorted(["flying", "poison", "bug", "steel", "fire", "grass", "dragon"]),
                                 "poison": sorted(["poison", "ground", "rock", "ghost"])},
        "defensive_weaknesses": sorted(["flying", "fire", "psychic", "ice"]),
        "immunities": [],
        "immune_defenders": {"grass": [], "poison": ["steel"]},
    }

    actual: Response = client.get('/weaknesses/summary/bUlBaSaUr')

    assert expected_summary == actual.json
    assert actual.status_code == 200


def test_get_weakness_summary_pokemon_not_found(client, example_pokemon):
    expected_response: dict[str, str] = {"message": "Pokemon not found"}
    actual: Response = client.get('/weaknesses/summary/bulba')

    assert expected_response == actual.json
    assert actual.status_code == 404


@patch("Application.Routes.Weakness.TypeUtils.get_weakness_summary",
       return_value={"error": "'Sound' is not a valid type"})
def test_get_mock_get_summary(mock_type_util, client, example_pokemon):
    expected_response: dict[str, str] = {"error": "'Sound' is not a valid type"}
    actual: Response = client.get('/weaknesses/summary/bulbasaur')

    mock_type_util.assert_called_once()
    assert actual.json == expected_response
    assert actual.status_code == 400


def test_get_weakness_summary_pokemon_empty_space(client, example_pokemon):
    expected_response: dict[str, str] = {"message": "Pokemon not found"}
    actual: Response = client.get('/weaknesses/summary/ ')

    assert actual.json == expected_response
    assert actual.status_code == 404
