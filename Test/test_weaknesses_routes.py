from unittest.mock import patch

import pytest
from flask import Response

from Application.Utils.TypeUtils import TypeUtils

type_util: TypeUtils = TypeUtils()


def assert_empty_response(client, route: str):
    expected_response: None = None
    actual: Response = client.get(f'/weaknesses/{route}')

    assert actual.json == expected_response
    assert actual.status_code == 404


def test_incomplete_weakness_route(client, example_pokemon):
    expected_response: None = None
    actual: Response = client.get('/weaknesses/')

    assert actual.json == expected_response
    assert actual.status_code == 404


# ============================================================
# /weaknesses/summary/<pokemon>
# ============================================================

def test_get_weakness_summary_pokemon_empty_str(client, example_pokemon):
    assert_empty_response(client, '/weaknesses/')


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


# ============================================================
# /weaknesses/offensive/<type>
# ============================================================

@pytest.mark.parametrize("bad_route", ["", "/", "fire/grass"])
def test_get_offensive_weakness_bad_route(client, bad_route):
    assert_empty_response(client, f'/weaknesses/offensive/{bad_route}')


@pytest.mark.parametrize('valid_type', ['fire', 'ghost', 'poison', 'FiRe', 'FIRE'])
def test_get_offensive_weakness_valid_types(client, valid_type):
    expected_list: list[str] = type_util.get_offensive_weaknesses(valid_type)
    expected_status: int = 200

    response: Response = client.get(f'/weaknesses/offensive/{valid_type}')
    actual_list: Response = response.json
    actual_status: int = response.status_code

    assert actual_list == expected_list
    assert actual_status == expected_status


@pytest.mark.parametrize("invalid_type", ["sound", " fire ", " "])
def test_get_offensive_weakness_invalid_type(client, invalid_type):
    expected_error_message: str = f"'{invalid_type.title()}' is not a valid type"
    expected_status: int = 404

    response: Response = client.get("/weaknesses/offensive/" + invalid_type)
    assert response.status_code == expected_status
    assert response.json.get("error") == expected_error_message


# ============================================================
# /weaknesses/defensive/<type>
# ============================================================
@pytest.mark.parametrize("bad_route", ["", "/"])
def test_get_defensive_weakness_bad_routes(client, bad_route):
    assert_empty_response(client, f'/weaknesses/defensive/{bad_route}')


@pytest.mark.parametrize('valid_type', ['fire', 'ghost', 'poison', 'FiRe', 'FIRE'])
def test_get_defensive_weakness_valid_types(client, valid_type):
    expected_list: list[str] = type_util.get_defensive_weaknesses(valid_type, type_2=None)
    expected_status: int = 200

    response: Response = client.get(f'/weaknesses/defensive/{valid_type}')
    actual_list: Response = response.json
    actual_status: int = response.status_code

    assert actual_list == expected_list
    assert actual_status == expected_status


@pytest.mark.parametrize("invalid_type", ["sound", " fire ", " "])
def test_get_defensive_weakness_invalid_type(client, invalid_type):
    expected_error_message: str = f"'{invalid_type.title()}' is not a valid type"
    expected_status: int = 404

    response: Response = client.get(f"/weaknesses/defensive/{invalid_type}")
    assert response.status_code == expected_status
    assert response.json.get("error") == expected_error_message


# ============================================================
# /weaknesses/defensive/<type>/<type>
# ============================================================
@pytest.mark.parametrize("bad_route", ["", "/", "ghost/water"])
def test_get_defensive_weakness_multitype_bad_routes(client, bad_route):
    assert_empty_response(client, f'/weaknesses/defensive/poison/{bad_route}')


@pytest.mark.parametrize('valid_type', ['fire', 'ghost', 'poison', 'FiRe', 'FIRE'])
def test_get_defensive_weakness_valid_multitype(client, valid_type):
    expected_list: list[str] = type_util.get_defensive_weaknesses("fire", valid_type)
    expected_status: int = 200

    response: Response = client.get(f'/weaknesses/defensive/fire/{valid_type}')
    actual_list: Response = response.json
    actual_status: int = response.status_code

    assert actual_list == expected_list
    assert actual_status == expected_status


@pytest.mark.parametrize("invalid_type", ["sound", " fire ", " "])
def test_get_defensive_weakness_invalid_multitype(client, invalid_type):
    expected_error_message: str = f"'{invalid_type.title()}' is not a valid type"
    expected_status: int = 404

    response: Response = client.get(f"/weaknesses/defensive/dragon/{invalid_type}")
    assert response.status_code == expected_status
    assert response.json.get("error") == expected_error_message

# ============================================================
# /weaknesses/immunities/<type>
# ============================================================

@pytest.mark.parametrize("bad_route", ["", "/", "fire/grass"])
def test_get_immunities_bad_route(client, bad_route):
    assert_empty_response(client, f'/weaknesses/immunities/{bad_route}')


@pytest.mark.parametrize('valid_type', ['fire', 'ghost', 'poison', 'FiRe', 'FIRE'])
def test_get_immunities_valid_types(client, valid_type):
    expected_list: list[str] = type_util.get_immunities(valid_type, None)
    expected_status: int = 200

    response: Response = client.get(f'/weaknesses/immunities/{valid_type}')
    actual_list: Response = response.json
    actual_status: int = response.status_code

    assert actual_list == expected_list
    assert actual_status == expected_status


@pytest.mark.parametrize("invalid_type", ["sound", " fire ", " "])
def test_get_immunities_invalid_type(client, invalid_type):
    expected_error_message: str = f"'{invalid_type.title()}' is not a valid type"
    expected_status: int = 404

    response: Response = client.get(f"/weaknesses/immunities/{invalid_type}")
    assert response.status_code == expected_status
    assert response.json.get("error") == expected_error_message

# ============================================================
# /weaknesses/immunities/<type>/<type>
# ============================================================

@pytest.mark.parametrize("bad_route", ["", "/", "fire/grass"])
def test_get_immunities_bad_route_dual_types(client, bad_route):
    assert_empty_response(client, f'/weaknesses/immunities/ghost/{bad_route}')


@pytest.mark.parametrize('valid_type', ['fire', 'ghost', 'poison', 'FiRe', 'FIRE'])
def test_get_immunities_valid_dual_types(client, valid_type):
    expected_list: list[str] = type_util.get_immunities("ghost", valid_type)
    expected_status: int = 200

    response: Response = client.get(f'/weaknesses/immunities/ghost/{valid_type}')
    actual_list: Response = response.json
    actual_status: int = response.status_code

    assert actual_list == expected_list
    assert actual_status == expected_status


@pytest.mark.parametrize("invalid_type", ["sound", " fire ", " "])
def test_get_immunities_invalid_dual_type(client, invalid_type):
    expected_error_message: str = f"'{invalid_type.title()}' is not a valid type"
    expected_status: int = 404

    response: Response = client.get(f"/weaknesses/immunities/ghost/{invalid_type}")
    assert response.status_code == expected_status
    assert response.json.get("error") == expected_error_message