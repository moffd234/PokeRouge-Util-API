from unittest.mock import patch

from flask import Response

from Application.Utils.TypeUtils import TypeUtils

type_util: TypeUtils = TypeUtils()


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


def test_get_offensive_weakness_empty_str(client):
    expected_response: None = None
    actual: Response = client.get('/weaknesses/offensive/')

    assert actual.json == expected_response
    assert actual.status_code == 404


def test_get_offensive_weakness_fire(client):
    expected_list: list[str] = type_util.get_offensive_weaknesses("fire")
    expected_status: int = 200

    response: Response = client.get('/weaknesses/offensive/fire')
    actual_list: Response = response.json
    actual_status: int = response.status_code

    assert actual_list == expected_list
    assert actual_status == expected_status

def test_get_offensive_weakness_ghost(client):
    expected_list: list[str] = type_util.get_offensive_weaknesses("ghost")
    expected_status: int = 200

    response: Response = client.get('/weaknesses/offensive/ghost')
    actual_list: Response = response.json
    actual_status: int = response.status_code

    assert actual_list == expected_list
    assert actual_status == expected_status

def test_get_offensive_weakness_mixed_case(client):
    expected_list: list[str] = type_util.get_offensive_weaknesses("ghost")
    expected_status: int = 200

    response: Response = client.get('/weaknesses/offensive/gHosT')
    actual_list: Response = response.json
    actual_status: int = response.status_code

    assert actual_list == expected_list
    assert actual_status == expected_status

def test_get_offensive_weakness_type_not_found(client):
    expected_error_message: str = "'Sound' is not a valid type"
    expected_status: int = 404

    response: Response = client.get('/weaknesses/offensive/sound')
    actual_error_message: Response = response.json["error"]
    actual_status: int = response.status_code

    assert actual_error_message == expected_error_message
    assert actual_status == expected_status


def test_get_offensive_weakness_trailing_slash(client):
    expected_response: None = None
    actual: Response = client.get('/weaknesses/offensive/fire/')

    assert actual.json == expected_response
    assert actual.status_code == 404

def test_get_offensive_weakness_valid_type_with_spaces(client):
    expected_error_message: str = "' Fire ' is not a valid type"
    expected_status: int = 404

    response: Response = client.get('/weaknesses/offensive/ fire ')
    actual_error_message: Response = response.json["error"]
    actual_status: int = response.status_code

    assert actual_error_message == expected_error_message
    assert actual_status == expected_status

def test_get_offensive_weakness_empty_space(client):
    expected_error_message: str = "' ' is not a valid type"
    expected_status: int = 404

    response: Response = client.get('/weaknesses/offensive/ ')
    actual_error_message: Response = response.json["error"]
    actual_status: int = response.status_code

    assert actual_error_message == expected_error_message
    assert actual_status == expected_status